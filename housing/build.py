"""Revision 2 enclosure and control extensions; millimeters, CadQuery 2.7.0."""
from pathlib import Path
import json
import math
import cadquery as cq

OUT = Path(__file__).parent
BATTERY = (66, 36, 11)
OUTER_R, INNER_R = 44, 41  # 3 mm nominal wall; retain screw bosses locally
# Vendor STEP coordinates: screen faces +Z; NOT a rear-view photograph.
MOUNTS = [(-29.5, 13.638), (29.5, 13.638), (-18, -27.06), (18, -27.06)]
CASE_SCREWS = [(40.7, 0), (0, 40.7), (-40.7, 0), (0, -40.7)]
BOARD_SHIFT = 25.5
SUPPORT_Z, SUPPORT_TOP = 17.0, 19.4
BUTTON_Y = (0.5023, 8.1023)  # reset, boot: actual +X actuator centers
BUTTON_Z = BOARD_SHIFT - 3.05
SLIDER_Y, SLIDER_Z = -7.303, BOARD_SHIFT - 3.1005
SLIDER_TRAVEL = 2.0
SLIDER_SOCKET_WIDTH, SLIDER_SOCKET_HEIGHT = 2.0, 1.3

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
# Cut USB windows BEFORE adding the supports: the old order notched the
# bottom pads by 1 mm. Pads stay flat at SUPPORT_TOP with unchanged centers.
for angle in (-45,-135):
    body=body.cut(radial_slot(angle,14,18.4,8.0))
# Four short bridges support the bottoms of the existing threaded M2 spacers.
# Screws enter from the battery compartment, upward into the board spacers.
for x,y in MOUNTS:
    a=math.degrees(math.atan2(y,x))
    r=math.hypot(x,y)
    bridge=box(OUTER_R-r+1,6,2.4,SUPPORT_Z,(OUTER_R+r-1)/2,0)
    bridge=bridge.rotate((0,0,0),(0,0,1),a)
    body=body.union(bridge).union(cyl(3.3,2.4,SUPPORT_Z,x,y))
    body=body.cut(cyl(1.2,4,SUPPORT_Z-0.5,x,y))
# Thin through-slits: tangential width x vertical height. Hidden inside reliefs
# accept the retaining collars; the exterior apertures stay thin.
body=body.cut(box(20,6.0,1.8,SLIDER_Z-0.9,38,SLIDER_Y))
body=body.cut(box(2.0,8.0,3.8,SLIDER_Z-1.9,38.5,SLIDER_Y))
for y in BUTTON_Y:
    body=body.cut(box(20,4.2,1.8,BUTTON_Z-0.9,38,y))
    body=body.cut(box(2.0,7.0,3.6,BUTTON_Z-1.8,38.5,y))
# Battery long axis follows Y; retain the confirmed pocket dimensions.
# 68 x 38 mm pocket between guides. No posts under the pouch.
for x in (-19.8,19.8):
    body=body.union(box(1.6,68,12.5,2.4,x,0))
    # join guide ends to the cylindrical wall; keep battery bay clear
    for y in (-36.0,36.0):
        body=body.union(box(3.2,6,12.5,2.4,math.copysign(20.6,x),y))
for x,y in CASE_SCREWS:
    # Blind pilot holes for separate front and rear M2.5 plastic screws.
    # Shorten front pilots to keep their tips above the control slits.
    body=body.cut(cyl(1.05,8,2.39,x,y)).cut(cyl(1.05,4.5,25.0,x,y))

back=cyl(OUTER_R,4.0)
for x,y in CASE_SCREWS:
    back=back.cut(cyl(1.4,5,-0.5,x,y))
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

# Reusable button extension. Local X is the press direction; thin stem passes
# outward through the slit from inside. An interior collar prevents loss outward.
# No enlarged exterior head: it would prevent insertion through a thin slit.
button=box(11.6,3.6,1.2,-0.6,40.0,0)  # X=34.2..45.8; 0.2 mm rest gap
button=button.union(box(1.2,6.0,3.0,-1.5,38.6,0))
# Slider: same inside-loading blade, with an inward-open socket over the black
# tab. Nominal tab 1.5 mm wide x 0.71 mm thick; pocket allows print clearance.
slider=box(10.3,3.0,1.2,-0.6,40.65,0)  # X=35.5..45.8
slider=slider.union(box(1.2,5.0,3.0,-1.5,38.6,0))
slider=slider.union(box(2.8,4.0,2.6,-1.3,34.6,0))
slider=slider.cut(box(2.5,SLIDER_SOCKET_WIDTH,SLIDER_SOCKET_HEIGHT,
                      -SLIDER_SOCKET_HEIGHT/2,33.95,0))

def print_orientation(part):
    # Lie each extension on its tangential side, preserving the socket opening.
    p=part.rotate((0,0,0),(1,0,0),90)
    b=p.val().BoundingBox()
    return p.translate((-b.xmin,-b.ymin,-b.zmin))

parts={'body':body.translate((0,0,-2.4)), 'rear_cover':back,
       'front_bezel':front, 'mount_fit_check':coupon,
       'power_slider':print_orientation(slider),
       'button_extension':print_orientation(button)}
# A small unchanged-in-scale section of the new control wall for cheap trials.
control_check=body.intersect(box(18,28,6.3,19.8,39,0))
b=control_check.val().BoundingBox()
parts['control_fit_check']=control_check.translate((0,0,-b.zmin))
# Check actual battery envelope plus 0.5 mm padding on every side.
battery_clearance=box(37,67,12,2.4,0,0)
assert body.intersect(battery_clearance).val().Volume()<1e-5,'battery interference'
# Full annular top of EVERY mounting pad must exist, not merely its hole center.
for x,y in MOUNTS:
    pad_top=cyl(3.3,0.15,SUPPORT_TOP-0.15,x,y).cut(cyl(1.2,0.3,SUPPORT_TOP-0.2,x,y))
    assert pad_top.cut(body).val().Volume()<1e-5,('pad not flat/full',x,y)
# Check both interchangeable buttons over free take-up and nominal actuation.
# These are housing collision checks, NOT a measured tactile-switch travel spec.
for y in BUTTON_Y:
    for travel in (0,0.2,0.4,0.6):
        placed=button.translate((-travel,y,BUTTON_Z))
        assert body.intersect(placed).val().Volume()<1e-5,('button blocked',y,travel)
for dy in (-SLIDER_TRAVEL/2,0,SLIDER_TRAVEL/2):
    assert body.intersect(slider.translate((0,SLIDER_Y+dy,SLIDER_Z))).val().Volume()<1e-5,('slider blocked',dy)
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
assembly.add(back.translate((0,0,-1.6)),name='rear_cover',color=cq.Color(0.35,0.40,0.45))
assembly.add(front.translate((0,0,29.4)),name='front_bezel',color=cq.Color(0.7,0.72,0.75))
assembly.add(slider.translate((0,SLIDER_Y+1,SLIDER_Z)),name='power_slider',color=cq.Color(0.8,0.5,0.2))
for i,y in enumerate(BUTTON_Y):
    assembly.add(button.translate((0,y,BUTTON_Z)),name=f'button_{i}',color=cq.Color(0.8,0.5,0.2))
assembly.save(str(OUT/'assembly.step'))
(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
