# Arc reactor housing — revision 3

For Waveshare **ESP32-S3-Touch-LCD-2.1B**, curved 71.8 mm glass, and a wrapped
**66 × 36 × 11 mm** LiPo. All dimensions are millimeters. Print at **100% scale**.
Nominal assembled envelope remains **88 mm diameter × 34 mm deep**, excluding
control blades and screw heads. The rear cover remains 4 mm thick, without LED holes.

## Revision 3 changes

- Cover fasteners are now at **12, 1:30, 4, 6, and 9 o'clock**, at the same
  40.7 mm radius. Body, front bezel, and rear cover all use this five-hole pattern.
  Clock positions are viewed from the screen/front, with the controls at 3 o'clock;
  the pattern appears mirrored when looking at the outside of the rear cover.
- The curved control wall is replaced with a **flat chord from 2 to 4 o'clock**,
  at the height of the controls only. The flat exterior is X = 38.105 mm,
  about 5.895 mm inside the outermost round rim, spanning approximately Y = ±22 mm.
  Its nominal thickness is 3 mm; local internal clearance pockets accept the
  extensions. The flat band runs from assembled Z = 20 to 25 mm.
- One-mm horizontal shoulders above and below that band join it to the round
  shell. The full circular front and rear rims are retained, rather than clipping
  the entire height of the housing. The bezel and rear cover stay fully round.
- Both control-extension models have revised collar locations for the flat wall.
  Their exterior tips remain beyond the round rims so they can be pressed.
- Power-slider travel is updated to the user's measured **2.03 mm**. Tab dimensions
  are **1.52 × 0.63 mm**, with its tip recessed **1.74 mm** from the glass edge.
  The socket reach now accounts for that recess; its clearance size remains
  2.0 mm wide × 1.3 mm high, with about 2 mm depth.

The confirmed board mounting-hole centers, flat M2 pad tops, battery guide faces,
USB opening locations, and rear battery clearance are retained. The 4 o'clock
fastener boss clears both the USB slot and the control area in CAD. **There is no
fastener at 3 o'clock.** No bosses are placed over the USB ports.

## What to print

Reprint **body, front bezel, rear cover, power slider, and two button extensions**.
The old bezel and rear cover have the wrong hole pattern for this revision.
Use the small **control_fit_check.stl** first to check the flat wall and extensions
before committing to a full new body. This coupon is a hand-aligned section of
the actual wall, not an installed part or a self-locating mount gauge.

Files:

- `body.stl`: revised shell, positioned on the print bed.
- `front_bezel.stl`: round bezel with five cover screw holes.
- `rear_cover.stl`: round 4 mm cover with five screw holes; no LED windows.
- `power_slider.stl`: print one, using the new measured tab reach.
- `button_extension.stl`: print **two identical copies**, for RESET and BOOT.
- `control_fit_check.stl`: small flat-control-wall trial piece.
- `mount_fit_check.stl`: original mounting-spacing gauge, unchanged.
- Matching `*.step` files and `assembly.step`: editable solid CAD.
- `preview.png`: technical views of actual exported STL meshes.
- `validation.json`, `mesh_validation.json`: solid and mesh check results.
- `arc_reactor_housing.zip`: bundle including the source and instructions.

## Printing

Suggested body settings: PLA or PETG, 0.2 mm layers, 0.4 mm nozzle, four perimeters,
20–30% infill. Print open side upward with **supports under mounting bridges and
under the projecting horizontal shoulders at the flat control band**. Remove all
supports before inserting electronics. Rear cover: flat. Front bezel: flat front
face downward, underside glass relief upward.

For the tiny extensions, PETG and 0.12–0.16 mm layers are suggested. The supplied
orientation lies each on its tangential side. Use supports under raised stems,
collars, and socket overhangs; not every underside touches the bed. Deburr and
compensate elephant foot so the 1.2 mm stems move freely in the 1.8 mm slits.
Do not force a fit with the board installed.

## Controls and assembly

The extensions have thin exterior blades and wider internal retaining collars.
Insert them from the inside before fitting the board. Their collars stay inside;
the board prevents them falling inward after assembly. They have no independent
return spring or calibrated overtravel stop: use light pressure, and verify that
neither RESET nor BOOT is held down at rest.

1. Trial-fit the control coupon and extensions against the board. Check slot
   height, slider engagement, and free travel before printing the full body.
2. Feed the stems outward through their slits, leaving collars inside. The
   slider socket opens inward toward the black tab. Lower the board in from the
   front and carefully engage that tab with the socket. Remove and adjust any
   extension that binds; do not force or glue the controls.
3. Attach the display using four **M2 × 4 mm pan-head machine screws**, inserted
   from the rear through the 2.4 mm support pads into the board's threaded spacers.
   Nominal engagement is about 1.6 mm; check actual thread depth and tighten gently.
4. Check both USB plugs insert fully and all three controls operate freely.
5. Fit the bezel with **five M2.5 × 6 mm screws suitable for plastic** through
   the 3 mm bezel. The body has 2.1 mm pilots, about 4.4 mm deep at the front.
   No washers or shorter bezel screws are required for this revised pattern.
6. Place the battery with its 66 mm axis along Y between the guide faces. Use
   removable nonconductive tape if needed; keep the pouch uncompressed and route
   wiring around an open guide end, clear of screws and actuator parts.
7. Fit the rear cover using **five M2.5 × 8 mm screws for plastic** through its
   4 mm thickness. Do not substitute longer screws without checking clearance.

The 3 o'clock screw from older versions is omitted. Do not drill extra holes
there or reuse old cover patterns. The rear cover's inner face is unchanged;
its 1.6 mm extra thickness relative to revision 1 grows outward.

## Measurements, assumptions and sources

Board mounting positions and battery fit were physically confirmed on earlier
prints. The previous button extensions nearly fitted. **Revision 3's flat band,
new fastener pattern, collars, and slider reach have not been physically fitted.**
The supplied checks establish geometric clearance, not actual switch travel limits
or printer tolerances.

Coordinate system: vendor STEP with screen facing +Z; translated +25.5 mm in Z.
Mount centers: (±29.5, 13.638), (±18, −27.060); pad tops Z = 19.4.
RESET/BOOT actuator centers: Y = 0.5023 / 8.1023, Z = 22.45, facing +X.
Slider center: Y = −7.303, Z = 22.3995; movement along Y. The measured recess is
interpreted along X from the local 71.8 mm glass edge; a radial interpretation
would change the estimated tip coordinate by only about 0.04 mm. That gives
roughly 1 mm insertion into the new socket. Physical socket fit still needs checking.

Vendor product and mechanical references:

- https://www.waveshare.com/esp32-s3-touch-lcd-2.1.htm
- https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_structure.zip
- https://www.waveshare.com/img/devkit/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1-details-size-1.jpg
- https://www.waveshare.com/img/devkit/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1-details-size-3.jpg

The vendor STEP represents standard 75 mm glass, not a dedicated B assembly.
The B glass diameter and the user's measurements override the relevant assumptions.
There are no rear-facing status LEDs; the actual status LEDs sit next to USB.
Costume attachment is not included.

## Rebuild and validation

The current workspace has Python, CadQuery 2.7.0, NumPy and Matplotlib. Use the
existing checkout; no Git worktree is needed. Run from the repository root:

```sh
XDG_CACHE_HOME=/tmp/cad-cache python housing/build.py
MPLCONFIGDIR=/tmp/matplotlib XDG_CACHE_HOME=/tmp/cad-cache python housing/inspect_meshes.py
```

The build checks valid single solids; a padded 37 × 67 × 12 mm battery envelope;
complete flat annular mounting-pad tops; control clearance over 0.6 mm button
movement and 2.03 mm slider travel; the flat wall and circular upper/lower rims;
and clearance of all five fastener bosses and bezel screw thread envelopes from
both USB openings. All seven STL meshes must have closed manifold edges,
consistent face winding, and positive signed volume. These checks do not replace
a slicer preview or physical fit test.
