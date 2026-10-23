"""Parametric first-fit enclosure; millimeters. Run with CadQuery 2.7.0."""
from pathlib import Path
import json
import math
import cadquery as cq

OUT = Path(__file__).parent
BATTERY = (66, 36, 11)
OUTER_R, INNER_R = 44, 39.2
# Vendor STEP coordinates: screen faces +Z; NOT a rear-view photograph.
MOUNTS = [(-29.5, 13.638), (29.5, 13.638), (-18, -27.06), (18, -27.06)]
CASE_SCREWS = [(40.7, 0), (0, 40.7), (-40.7, 0), (0, -40.7)]
BOARD_SHIFT = 25.5
SUPPORT_Z, SUPPORT_TOP = 17.0, 19.4

def cyl(r, h, z=0, x=0, y=0):
    return cq.Workplane('XY').workplane(offset=z).center(x, y).circle(r).extrude(h)

def box(x, y, h, z=0, cx=0, cy=0):
    return cq.Workplane('XY').workplane(offset=z).center(cx, cy).box(x,y,h,centered=(True,True,False))

def radial_slot(angle, width, z, height, start=28):
    # local X is outward along the plug insertion direction.
    return box(25,width,height,z,start+12.5,0).rotate((0,0,0),(0,0,1),angle)

body = cyl(OUTER_R,27,2.4).cut(cyl(INNER_R,29,1.4))
for x,y in CASE_SCREWS:
    body=body.union(cyl(3.0,27,2.4,x,y))
# Four short bridges support the bottoms of the existing threaded M2 spacers.
# Screws enter from the battery compartment, upward into the board spacers.
for x,y in MOUNTS:
    a=math.degrees(math.atan2(y,x))
    r=math.hypot(x,y)
    bridge=box(OUTER_R-r+1,6,2.4,SUPPORT_Z,(OUTER_R+r-1)/2,0)
    bridge=bridge.rotate((0,0,0),(0,0,1),a)
    body=body.union(bridge).union(cyl(3.3,2.4,SUPPORT_Z,x,y))
    body=body.cut(cyl(1.2,4,SUPPORT_Z-0.5,x,y))
# USB ports point diagonally outward toward the bottom corners.
for angle in (-45,-135):
    body=body.cut(radial_slot(angle,14,18.4,8.0))
# Switch on +X in STEP coordinates (left when looking at the rear).
body=body.cut(box(19,14,9,18.3,37.5,-7.3))
# Additional BOOT/RESET tool-access openings, separate from the switch.
for y in (4.338,-4.582):
    body=body.cut(box(19,4.5,4.5,20.0,37.5,y))
# Battery long axis follows Y; keeps both status LED sightlines clear.
# 68 x 38 mm pocket between guides. No posts under the pouch.
for x in (-19.8,19.8):
    body=body.union(box(1.6,68,12.5,2.4,x,0))
    # join guide ends to the cylindrical wall; keep battery bay clear
    for y in (-34.5,34.5):
        body=body.union(box(3.2,3,12.5,2.4,math.copysign(20.6,x),y))
for x,y in CASE_SCREWS:
    # Blind pilot holes for separate front and rear M2.5 plastic screws.
    body=body.cut(cyl(1.05,8,2.39,x,y)).cut(cyl(1.05,8,21.41,x,y))

back=cyl(OUTER_R,2.4)
for x,y in CASE_SCREWS:
    back=back.cut(cyl(1.4,4,-0.5,x,y))
# Two rear status windows outside the battery footprint. Enlarged for sightline.
for x,y in [(29.2,-17.8),(31.2,-14.1)]:
    back=back.cut(cyl(2,4,-0.5,x,y))
# Wire routing notch in battery guide is implicit at the open short ends.
front=cyl(OUTER_R,3).cut(cyl(35.4,5,-1))
# Underside relief: 72.6 mm diameter for the nominal 71.8 mm curved panel.
front=front.cut(cyl(36.3,0.8,-0.01))
for x,y in CASE_SCREWS:
    front=front.cut(cyl(1.4,5,-1,x,y))

# Inexpensive mount-spacing check, held against exposed spacer ends.
coupon=cyl(35,1.2).cut(cyl(25,3,-1))
for x,y in MOUNTS:
    coupon=coupon.union(cyl(3.3,1.2,0,x,y))
    coupon=coupon.cut(cyl(1.2,3,-1,x,y))

parts={'body':body.translate((0,0,-2.4)), 'rear_cover':back,
       'front_bezel':front, 'mount_fit_check':coupon}
# Check actual battery envelope plus 0.5 mm padding on every side.
battery_clearance=box(37,67,12,2.4,0,0)
assert body.intersect(battery_clearance).val().Volume()<1e-5,'battery interference'
# Direct sightlines from rear cover to the rear-facing status LEDs.
for x,y in [(29.2,-17.8),(31.2,-14.1)]:
    assert body.intersect(cyl(1.0,20,2.4,x,y)).val().Volume()<1e-5,'LED blocked'
report={}
for name,part in parts.items():
    shape=part.val()
    assert shape.isValid(),name
    assert len(part.solids().vals())==1,(name,'disconnected solids')
    assert shape.Volume()>0,name
    cq.exporters.export(part,str(OUT/f'{name}.stl'),tolerance=0.04,angularTolerance=0.1)
    cq.exporters.export(part,str(OUT/f'{name}.step'))
    b=shape.BoundingBox()
    report[name]={'valid':True,'solids':1,'size_mm':[round(b.xlen,3),round(b.ylen,3),round(b.zlen,3)],'volume_mm3':round(shape.Volume(),2)}
assembly=cq.Assembly(name='arc_reactor')
assembly.add(body,name='body',color=cq.Color(0.20,0.24,0.28))
assembly.add(back,name='rear_cover',color=cq.Color(0.35,0.40,0.45))
assembly.add(front.translate((0,0,29.4)),name='front_bezel',color=cq.Color(0.7,0.72,0.75))
assembly.save(str(OUT/'assembly.step'))
(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
