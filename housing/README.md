# Arc reactor housing — revision 6

Waveshare **ESP32-S3-Touch-LCD-2.1B**, 71.8 mm curved glass, with a wrapped
**66 × 36 × 11 mm** LiPo. Dimensions in millimeters; print at **100% scale**.
The round case remains **88 mm diameter × 34 mm deep**, excluding controls.
The top lanyard lug increases the overall height to approximately **97 mm**.

## Revision 6: easier-fitting power-slider cap

**Only `power_slider_cap.stl` needs reprinting.** The body, slider carriage,
button extensions, bezel, rear cover and test coupon remain unchanged.

The cap socket is now **3.3 × 1.5 mm**, increased from **2.95 × 1.15 mm** for
its **3.0 × 1.2 mm** stem. This gives **0.15 mm nominal clearance per side**
instead of interference. A **3.7 × 1.9 mm tapered entry** narrows over 0.35 mm
into the socket to make insertion easier. Socket depth, insertion shoulder,
exterior grip and guide wings remain unchanged.

This is a clearance fit, not a guaranteed friction/press fit. The external L rails
capture the cap and the carriage stem couples its sideways movement; a small
amount of fit play is expected. Printer shrinkage and hole sizing can still vary.
Try it with the printed carriage and control coupon before fitting the board.
Keep the original assembly order: slide the cap into the rails from the side,
then insert the carriage stem from inside with the board removed. Do not force
the fit or push against the board switch. The new socket passes a CAD check for
zero solid interference with the complete seated carriage.

## Revision 5: rear-edge lanyard attachment at 12 o'clock

Only **body.stl** needs reprinting for this change. Revision 4 control parts,
bezel, rear cover, and test coupon are unchanged and compatible.

A reinforced external lug is centered at **12 o'clock**, toward the **rear-cover
edge (bottom in Z)**. It has two **4 mm through-holes**, **10 mm center-to-center**,
with 0.5 mm rounded entrances to reduce cord abrasion. Its rounded root is
22 mm wide and the lug is 6 mm thick. The lug begins **1 mm above the rear-cover
mating plane**, leaving the cover free to install. It extends 9 mm beyond the
round top edge, so the bores and tether remain outside the electronics cavity.
The 12 o'clock cover screw pilot is retained and clear.

Thread a thin lanyard cord through the two holes to form a tether attachment;
deburr the printed entrances. Support the underside of the lug when printing
(the underside is 1 mm above the print bed in the supplied body orientation).
PETG and at least four perimeters are suggested. This attachment has not been
load-tested; check the printed root and test with a gentle pull before use.
For a child's costume, use a **breakaway lanyard**.

The build checks both bores are open and outside the cavity, battery clearance,
and the usual control/fastener clearances. Mesh closure is also checked. These
checks do not establish a catch-load rating for the printed attachment.

## Revision 4 changes

- The flat control well is now **15 mm tall in Z**, from assembled Z = 10.5 to
  25.5, instead of the previous 5 mm. The flat face remains at X = 38.105, the
  chord between 2 and 4 o'clock. Full round front/rear rims remain, joined by
  1 mm horizontal shoulders. The upper shoulder ends at Z = 26.5, below the
  standard vendor glass envelope starting at Z = 26.7.
- The two push-button extensions are shortened from **10.6 to about 5.3 mm**,
  ending 1.4 mm outside the flat wall. Print the same new file twice.
- The power-slider extension now has a **6 × 3.8 mm internal bearing plate**
  running in a close-clearance recess. Its socket position/size remains the
  physically tested revision 3 geometry: 2.0 × 1.3 mm opening, about 2 mm depth.
- A new **outer cap** has an 8 mm wide grip and thin wings captured
  beneath two external L rails. These rails and the internal bearing plate
  resist rocking, so the switch tab no longer supplies the entire guiding force.
- A shoulder sets cap insertion depth. Nominal cap-to-wall and wing-to-lip gaps
  are 0.3 mm. Vertical wing clearance is 0.25 mm per side. The inner plate has
  0.3 mm clearance per side; its recess permits 2.63 mm total movement around
  the measured 2.03 mm switch travel. These small clearances permit some play;
  the design is not intended to be a zero-clearance clamp.

The five cover fasteners remain at **12, 1:30, 4, 6, and 9 o'clock**, viewed from
the screen/front with the controls on the right. USB openings, board mounting
centers, flat M2 seating pads, battery guide faces, and rear cover thickness are
retained. **Revision 3 front bezel and rear cover can be reused.**

## Files to print

- `body.stl`: new body with the wider well, inner carriage recess and outer rails.
- `button_extension.stl`: **print two**, for RESET and BOOT.
- `power_slider.stl`: **print one** new carriage/extension.
- `power_slider_cap.stl`: **print one** clearance-fit outer cap.
- `control_fit_check.stl`: **print this first** to test the carriage, cap and
  shorter buttons before committing to another complete body. It is a cutout
  of the actual new control wall, not a self-locating board-mount gauge.

Also supplied: unchanged `front_bezel.stl`, `rear_cover.stl` and mounting gauge;
matching STEP files; complete `assembly.step`; a smaller `control_test_assembly.step`
showing the coupon/carriage/cap assembled; `preview.png`; solid/mesh validation
reports; and both STL-only and full-source ZIP bundles.

**Use all three new slider parts together**: new body (or coupon), new carriage,
and new cap. Revision 3 collars/stems do not suit the new captured guide.

## Important assembly order for the captured cap

The cap's wings cannot be pushed straight through the overhanging L rails.
They must enter from an open end, before attaching the stem:

1. Remove supports and deburr the coupon/body guide surfaces. Keep all mating
   surfaces free of elephant foot and loose strands.
2. With **the board out**, slide the cap **along Y** into the outside L rails,
   entering from the end nearest USB (negative Y). The thin wing plate faces
   the wall, the thicker grip faces out, and the bore opens toward the wall.
3. Insert the internal carriage from inside the housing. Align its short stem
   with the cap bore and press them together until the cap meets the stem's
   shoulder. Support the carriage and cap directly while doing this. **Do not
   use the board switch as the backstop for press-fitting.**
4. Check the assembled carriage/cap moves sideways freely. It should not clamp
   the wall or rub the rail lips. The internal pocket gives a small margin beyond
   the board's measured 2.03 mm travel; it does not establish the switch's safe
   force or overtravel rating. Do not force the mechanism against an end stop.
5. Feed the two new push-button stems outward from inside, collars remaining in.
6. Lower the board in from the front and carefully engage the black switch tab
   in the carriage's inward-open socket. Attach the board, then verify both
   power positions and that RESET/BOOT release fully after light presses.
7. Close the bezel and rear cover only after the controls and USB plugs work freely.

The cap bore uses the revision 6 clearance fit described above. If the printed
socket still binds, check for support residue or elephant foot before adjusting
its dimensions in `build.py`. Do not force the mechanism with the board installed.
The socket coupling to the board switch remains unchanged.

The push buttons still rely on the board's own tactile switches for return force;
there is no independent spring or calibrated overtravel stop. Use light pressure.

## Printing

Suggested body: PLA or PETG, 0.2 mm layers, 0.4 mm nozzle, four perimeters,
20–30% infill. Print with the front opening upward. **Support the mounting
bridges, the horizontal well shoulders, and the external L-rail overhangs.**
Clean supports out of the inner carriage recess and from beneath the rail lips.

For the tiny control parts, PETG and 0.12–0.16 mm layers are suggested. Slider
and push-button STLs lie on their tangential sides; their stems/plates have raised
undersides and need small supports. The cap is oriented grip-face down with its
bore opening upward; support the wing overhangs if needed, but keep the bore
free of support material. Inspect the slicer preview to verify the bore remains
open. Rear cover: flat. Bezel: flat front face downward, relief upward.

## Screws and battery

- Display: four **M2 × 4 mm pan-head machine screws** through 2.4 mm mounting
  pads into the existing threaded spacers. Nominal engagement 1.6 mm; verify
  actual depth and tighten gently.
- Bezel: five **M2.5 × 6 mm screws for plastic** through the 3 mm bezel.
- Rear cover: five **M2.5 × 8 mm screws for plastic** through the 4 mm cover.

Keep the battery's 66 mm axis along Y between the guide faces. Retain it with
removable nonconductive tape if needed, without compressing the pouch. Route
wires around an open guide end, clear of fasteners and moving control parts.
There are no rear LED windows. Costume attachment is not included.

## Evidence and limitations

The user has physically confirmed the revision 3 case, button alignment, slider
socket fit and reach. That long unsupported slider could rotate around the switch;
the revision 4 bearings and captured cap specifically address that failure.
**Revision 4 has not yet been physically printed or tested.** Finger access and
socket tolerances must be checked on the included small coupon.

User measurements: tab **1.52 × 0.63 mm**, travel **2.03 mm**, tab tip **1.74 mm**
inside the glass edge. Recess is interpreted along X from the local 71.8 mm glass
edge; interpreting it radially changes the estimate by only about 0.04 mm.
Coordinates follow the vendor model with screen facing +Z, shifted +25.5 mm in Z.
M2 centers remain (±29.5, 13.638), (±18, −27.060), pad tops Z = 19.4.
RESET/BOOT: Y = 0.5023 / 8.1023, Z = 22.45. Slider: Y = −7.303,
Z = 22.3995, movement along Y. The upper well edge is limited by display clearance;
the added finger space is primarily below the original control height.

Vendor references:

- https://www.waveshare.com/esp32-s3-touch-lcd-2.1.htm
- https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_structure.zip
- https://www.waveshare.com/img/devkit/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1-details-size-1.jpg

## Rebuilding and checks

Current environment: Python, CadQuery 2.7.0, NumPy, Matplotlib. Use the existing
checkout; no Git worktree is needed. Run from the repository root:

```sh
XDG_CACHE_HOME=/tmp/cad-cache python housing/build.py
MPLCONFIGDIR=/tmp/matplotlib XDG_CACHE_HOME=/tmp/cad-cache python housing/inspect_meshes.py
```

Build checks include valid single solids; padded battery clearance; complete flat
mounting-pad tops; full nominal slider and button movement; cap clearance during
side-loading into rails; small axial bearing play; positive guide contact when
attempting to pull the cap out or displace it vertically; retained flat wall and
circular rims; and USB clearance from all cover bosses and screw envelopes.
All eight meshes must have closed manifold edges, consistent face winding and
positive volume. Results: `validation.json` and `mesh_validation.json`. CAD checks
cannot prove actual friction, return force, press-fit strength or finger comfort.
