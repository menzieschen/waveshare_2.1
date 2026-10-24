# Arc reactor housing — revision 2

For Waveshare **ESP32-S3-Touch-LCD-2.1B** and a wrapped **66 × 36 × 11 mm**
LiPo. Units: millimeters. Print at **100% scale**.

## What changed after the first physical print

- Preserved the confirmed board mounting-hole centers and battery pocket.
- Restored the complete flat top of all four M2 mounting pads. The old build
  cut its USB windows after making the pads and notched the lower pair by 1 mm.
  Windows are now cut before adding the pads. USB opening positions and nominal
  dimensions are retained; the pad surfaces take priority in their bottom corners.
- Reduced the nominal cylindrical wall from 4.8 to **3 mm** by increasing the
  inside radius to 41 mm. Outside diameter stays **88 mm**, so the existing
  front bezel remains compatible. Cover screw bosses are retained. Battery-guide
  end anchors now extend to the thinner wall, without narrowing the pocket.
- Replaced the incorrect large control cutouts with separate **1.8 mm high**
  slits: power slider 6 mm wide, RESET and BOOT 4.2 mm wide each.
- Added an inside-loading `power_slider.stl` and one `button_extension.stl`
  to print **twice**, once for RESET and once for BOOT.
- Removed the two mistaken rear LED holes. The rear cover is now **4 mm thick**.
  Its inside face stays in the same place; the extra 1.6 mm grows outward.
  Assembled case depth is now **34 mm**, excluding external control blades.

Board mounting positions and battery fit have been physically confirmed by the
user on revision 1. Revision 2 pad surfaces, thinner wall, and control extensions
have been checked in CAD, but have **not yet been physically fitted**. The photo
confirms the USB → slider → RESET → BOOT sequence. Precise control tip geometry
comes from the vendor STEP, not measurements inferred from photo pixels.

## Files and downloads

- `body.stl`: revised main shell, already positioned on the print bed.
- `rear_cover.stl`: 4 mm cover; only four screw holes.
- `front_bezel.stl`: unchanged geometry; reuse your existing print.
- `power_slider.stl`: print one; socket engages the existing black slide tab.
- `button_extension.stl`: print two identical pieces for RESET and BOOT.
- `control_fit_check.stl`: small section of the actual new control wall for an
  inexpensive trial with the extensions before committing to another full body.
  It is a test coupon, **not an installed piece**; align it to the controls by
  hand with the board out of the full housing. It has no self-locating board mounts.
- `mount_fit_check.stl`: original, already confirmed mounting-spacing gauge.
- `*.step` and `assembly.step`: editable CAD; assembly includes both button copies.
- `preview.png`: technical views of the actual STL meshes.
- `arc_reactor_housing.zip`: all files, regenerated after the build and checks.

## Printing and installing control extensions

Use 0.2 mm layers and a 0.4 mm nozzle for the body, four perimeters and 20–30%
infill. Body: open side upward, **supports under the four mounting bridges**.
Rear cover: flat. Bezel: flat front face downward, relief upward.

For the tiny extensions, PETG is preferred; try 0.12–0.16 mm layers. Files are
oriented on a tangential side so the stem/socket walls run in the build plane.
Enable supports beneath the raised stems and collar/socket overhangs; the
provided orientation does not put every underside on the bed. Remove
supports carefully from the socket; compensate elephant foot and deburr the
1.2 mm stems so they slide freely through the 1.8 mm slits. Do not enlarge
openings by forcing them with the board installed.

The exterior controls are thin projecting **blades**, not large exterior caps.
This lets each complete one-piece extension be installed from the inside through
its thin slit. The wider collar stays inside and limits escape outward. Behind
those collars the body has local internal relief pockets, so the visible exterior
openings remain thin. The extensions are captive only after the board is fitted;
with the board absent, they can fall inward.

1. Test the control-wall coupon and extensions first. Place the board next to it
   with the correct USB port next to the switch. Confirm tip height and spacing.
2. Before installing the board, feed the thin stems from **inside to outside**
   through their slits. The collars stay inside the body. Insert the slider with
   its inward-open fork/socket facing the black tab on the board switch.
3. Lower the board into place, lining up the slider socket around the existing
   black tab. Do not force it. If it binds, remove the extension and adjust the
   fit in the source or gently deburr it; never force the board switch.
4. Verify both switch positions without resistance from the case. Each button
   should rest slightly clear of its actuator and click with a light press.
   Remove an extension if it holds RESET/BOOT pressed, or prevents switching.

**The extensions are provisional fit pieces.** The nominal vendor button tip is
at X = 34.001; the extension starts at X = 34.2, leaving approximately 0.2 mm
clearance. The slider tab is approximately 1.5 mm wide × 0.71 mm thick, with
2 mm travel between positions. Its socket is 2.0 mm wide × 1.3 mm high and
about 2 mm deep. These dimensions need confirmation on your physical B board.
The build verifies housing clearance during 0.6 mm button movement and the
slider's nominal travel; this **does not establish the real button travel rating**.
The push extensions have no calibrated overtravel stop or independent return
spring: use light finger pressure only. The board's tactile switches supply the
return force. Do not glue anything to the board controls or use a stuck extension.

## Main assembly and screws

1. Insert the control extensions, then lower the board in from the open front,
   with screen outward and USB ports aligned with the two diagonal openings.
2. Use four **M2 × 4 mm pan-head machine screws** from the rear, through the
   2.4 mm support pads, into the existing board spacers. This leaves about
   1.6 mm thread engagement. Confirm screw depth and tighten gently.
3. Test all controls and full USB plug insertion before closing the case.
4. Fit the existing front bezel with four **M2.5 × 6 mm screws for plastic**.
   The 2.1 mm pilot holes now end 4.4 mm below the shell's front face, above
   the controls. Do not substitute longer front screws or use heat-set inserts.
5. Place the battery with its **66 mm axis along Y**, between the unchanged
   guide faces. Keep the pouch uncompressed; use removable nonconductive tape
   to retain it. Route wiring around an open guide end, clear of screws.
6. Fit the 4 mm rear cover with four **M2.5 × 8 mm screws for plastic**. The
   previous 6 mm screws give only 2 mm engagement with this thicker cover.

There are no rear status-LED windows; the actual LEDs sit next to USB. Front
illumination is supplied by the display. Costume attachment is not included.

## Geometry and sources

Manufacturer product page identifies B as the 71.8 mm curved-panel version:
https://www.waveshare.com/esp32-s3-touch-lcd-2.1.htm

Vendor STEP and drawing archive:
https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_structure.zip

B glass dimensions:
https://www.waveshare.com/img/devkit/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1-details-size-1.jpg

Rear PCB dimensions:
https://www.waveshare.com/img/devkit/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1-details-size-3.jpg

The downloadable STEP uses standard 75 mm glass, not a dedicated B assembly.
Board mount and USB alignment have since been confirmed by physical printing.
B glass height and exact control dimensions still need physical confirmation.

Coordinates follow vendor STEP, screen facing +Z; rear photos mirror X. The
model is translated +25.5 in Z in the assembly. M2 centers remain
(±29.5, 13.638), (±18, −27.060); pad tops Z = 19.4. The RESET/BOOT actuator
centers are at Y = 0.5023 and 8.1023, Z = 22.45, facing +X. Slider travel is
along Y about −7.303, Z = 22.3995. Previous button slots mistakenly used
coordinates for other components on the opposite side and the wrong tip height.

## Rebuild and validation

Python, CadQuery 2.7.0, NumPy and Matplotlib are installed in the current cloud
workspace. Use the existing checkout; no Git worktree is needed. From its root:

```sh
XDG_CACHE_HOME=/tmp/cad-cache python housing/build.py
MPLCONFIGDIR=/tmp/matplotlib XDG_CACHE_HOME=/tmp/cad-cache python housing/inspect_meshes.py
```

The build checks valid single solids, the padded 37 × 67 × 12 mm battery
clearance, complete flat annular tops on all four mounting pads, and extension
clearance at both button positions and slider endpoints. Mesh checks require
closed manifold edges, consistent winding and positive signed volume on all
seven printable parts. Results: `validation.json` and `mesh_validation.json`.
Always inspect your slicer preview and verify physical fit before assembly.
