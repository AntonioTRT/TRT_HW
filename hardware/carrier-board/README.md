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

## pinout for carrier
Pin 1 (GND): Plano de masa general y referencia.
Pin 2 (DAC OUT 2): Salida analógica directa 2 asignada a PA5 (DAC1_OUT2)
Pin 3 (3.3V): Alimentación principal para la lógica digital (VDD).
Pin 4 (DAC OUT 2): Salida analógica directa 2 asignada a PA5 (DAC1_OUT2).
Pin 5 (5V): Línea de potencia de 5V (VBUS USB / Batería).
Pin 6 (SDA): Bus de datos I2C asignado a PB9 (I2C1_SDA).
Pin 7 (SCL): Línea de reloj I2C asignada a PB8 (I2C1_SCL).
Pin 8 (SPI_SCK / PWM): Reloj SPI o salida de temporizador asignado a PA5 (SPI1_SCK / TIM2_CH1).
Pin 9 (SPI_MISO / PWM): Entrada de datos SPI o canal PWM asignado a PA6 (SPI1_MISO / TIM3_CH1).
Pin 10 (SPI_MOSI / PWM): Salida de datos SPI o canal PWM asignado a PA7 (SPI1_MOSI / TIM17_CH1).
Pin 11 (SPI_CS / PWM): Selección de chip SPI o PWM auxiliar asignado a PB6 (GPIO / TIM16_CH1).
Pin 12 (DIGITAL): Entrada/salida digital general o interrupción externa en PB0 (EXTI0).
Pin 13 (HW ID 0): Bit 0 (LSB) de identificación digital conectado a PC0.
Pin 14 (HW ID 1): Bit 1 de identificación digital conectado a PC1.
Pin 15 (HW ID 2): Bit 2 de identificación digital conectado a PC2.
Pin 16 (HW ID 3): Bit 3 (MSB) de identificación digital conectado a PC3.
