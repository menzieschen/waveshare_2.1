# Arc reactor housing — first-fit prototype

Target: Waveshare **ESP32-S3-Touch-LCD-2.1B**, curved 71.8 mm glass,
and a wrapped **66 × 36 × 11 mm** LiPo battery. All dimensions are millimeters.
Nominal assembled envelope: **88 mm diameter × 32.4 mm deep**, without screws.

This is a CAD-validated prototype, not a physically verified fit. Print
`mount_fit_check.stl` first and hold it against the four exposed threaded spacer
ends on your board. The exact B glass height and cable-overmold fit still need
checking on your device. Do not force the glass, spacers, or battery into place.

## Files

- `body.stl`: main shell, USB-C/switch/button cutouts, four board supports,
  battery guides, and cover screw pilots. Already positioned on the print bed.
- `front_bezel.stl`: separate face ring, 70.8 mm opening and 72.6 mm underside relief.
  The active screen is about 53.48 mm across, so its full area remains visible.
- `rear_cover.stl`: removable battery access cover, with two 4 mm status-LED windows.
  LEDs shine toward the rear; the battery guides leave their sightlines clear.
- `mount_fit_check.stl`: 1.2 mm thick spacing gauge; **not an installed part**.
- Matching STEP files and `assembly.step`: editable solid geometry.
- `preview.png`: view of the exported STL meshes.
- `build.py`: parameterized CadQuery source; `inspect_meshes.py`: mesh checks/preview.

## Printing

Suggested starting settings: PETG or PLA, 0.2 mm layers, 0.4 mm nozzle,
4 perimeters, 20–30% infill. Body: open side up, **supports under the four
internal mounting bridges**; remove supports before installing electronics.
Rear cover: flat. Front bezel: put its flat front face on the bed, relief upward.
Print the fit gauge first. Printer shrinkage/hole tolerances may require adjustment.
Hole centers must be retained if increasing hole diameters in the source.

## Assembly

1. Check the gauge aligns with the board's four threaded M2 spacer ends.
2. With rear cover and bezel removed, lower the board through the front of the
   shell, screen facing outward, USB-C connectors toward the two diagonal slots.
   In CAD coordinates, USB is at negative Y and the switch is at positive X.
3. Fit four **M2 × 4 mm machine screws** from the rear through the support holes
   into the existing board spacers. The supports are 2.4 mm thick, leaving about
   1.6 mm thread engagement. Confirm the actual spacer thread depth before use;
   account for washers and never bottom a screw out against electronics.
4. Verify both USB plugs insert fully, the switch moves through its full travel,
   and BOOT/RESET are accessible. USB slots are 14 mm wide × 8 mm high; some
   cable housings may need larger openings. Switch opening is 14 × 9 mm.
5. Fit the front bezel with four **M2.5 × 6 mm screws suitable for plastic**.
   The body has 2.1 mm pilot holes. Tighten lightly; do not clamp the glass.
   No heat-set inserts or M2.5 machine-threaded holes are provided.
6. Lay the battery with its **66 mm axis along Y**, centered between the guides.
   Nominal pocket is 68 × 38 mm; at least a 37 × 67 × 12 mm padded envelope
   is checked clear in CAD. Use removable nonconductive tape to retain it.
   Route the lead around a guide's open short end, clear of screws and edges.
   Keep the pouch uncompressed, with no screw tips or electronics against it.
7. Fit the rear cover with four more M2.5 × 6 mm plastic screws. Verify the two
   status LEDs can be seen through the rear windows. Those windows are for
   status visibility, not front-facing arc-reactor illumination.

Cover screw pilots are blind and separate at each end. Battery access requires
removing the rear cover. Costume attachment is not included in this first design.

## Geometry and sources

Manufacturer product page identifies the B curved-panel version:
https://www.waveshare.com/esp32-s3-touch-lcd-2.1.htm

Manufacturer mechanical drawing archive (standard board assembly):
https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1_structure.zip

B glass diameter drawing:
https://www.waveshare.com/img/devkit/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1-details-size-1.jpg

Rear board dimensions:
https://www.waveshare.com/img/devkit/ESP32-S3-Touch-LCD-2.1/ESP32-S3-Touch-LCD-2.1-details-size-3.jpg

The downloadable STEP is the **standard 75 mm glass assembly**, not a dedicated
B assembly. Board mounting, connector, switch and LED coordinates were taken
from that model, while the bezel uses the published B glass diameter.
Shared PCB geometry is a first-fit assumption requiring physical confirmation.
The shell accommodates the standard 75 mm glass envelope as clearance, but the
bezel is intended for B. Do not treat this as a confirmed universal-fit enclosure.

Coordinate system follows vendor STEP: screen faces +Z; rear-view photographs
mirror X. M2 mounting centers: (±29.5, 13.638), (±18, −27.060).
Spacer bottoms are at Z = 19.4 in assembled housing coordinates. Vendor model
is translated +25.5 in Z. LED window centers: (29.2, −17.8), (31.2, −14.1).

## Rebuilding and checks

Current environment has Python, CadQuery 2.7.0, NumPy and Matplotlib installed.
From the repository root:

```sh
XDG_CACHE_HOME=/tmp/cad-cache python housing/build.py
MPLCONFIGDIR=/tmp/matplotlib python housing/inspect_meshes.py
```

The build checks valid single solids, battery clearance, and unobstructed LED
sightlines. Mesh checks require every edge to have exactly two incident faces,
consistent winding, and positive signed volume. Results are in `validation.json`
and `mesh_validation.json`. These checks do not replace a slicer preview or a
physical fit test. STL units are millimeters; do not scale on import.
