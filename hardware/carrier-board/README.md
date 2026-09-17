# STM32G474 Carrier Board

This folder contains the KiCad 8 project files for the STM32G474RET6 carrier board.

## Contents

- `carrier-board.kicad_pro` - KiCad project file for the carrier board.
- `carrier-board.kicad_sch` - Main KiCad schematic file (defines sheet structure).
- `power_usb.kicad_sch` - Schematic page for Power and USB sections.
- `mcu_core.kicad_sch` - Schematic page for MCU, Debug, and Reset.
- `peripherals.kicad_sch` - Schematic page for LEDs and Encoder.
- `expansion.kicad_sch` - Schematic page for the expansion connector.
- `carrier-board.kicad_pcb` - KiCad PCB board file.

## Board overview

This carrier board is intended for the STM32G474RET6 MCU with the following main sections:

- USB-C power and data connector
- 3.3V LDO power supply (AP2112K-3.3)
- MCU decoupling and reset circuitry
- Debug SWD via Tag-Connect TC2030-NL footprint
- RGB LED ring (SK6812) and Rotary Encoder
- 2x10 Board-to-Board expansion header

## Notes

- This project was initialized for KiCad 8.
- The schematic is organized into a flat, multi-page structure.
- The PCB file is pre-configured with a 4-layer stackup, 50x50mm board outline, and M2.5 mounting holes.
- Components have been added to the schematic but require wiring. They have been imported into the PCB but require placement and routing.
- LCSC part numbers are included as custom fields in the schematic symbols for reference.

## How to open

1. Open KiCad 8 or newer.
2. Open `hardware/carrier-board/carrier-board.kicad_pro`.
3. The schematic pages and board file will be accessible from the project tree.
