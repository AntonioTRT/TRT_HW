# STM32G474 Carrier Board

This folder contains the KiCad project files for the STM32G474RET6 carrier board.

## Board Overview

This carrier board is built around the STM32G474RET6 MCU (LQFP64) designed with 0805 SMD components for manual soldering and JLCPCB assembly compatibility. Main hardware features include:

- **USB-C Interface:** USB 2.0 Full-Speed (PA11/PA12) with dual 5.1kΩ CC1/CC2 pull-down resistors for Type-C power negotiation.
- **Power Supply:** +5V VBUS input regulated to +3.3V via AMS1117-3.3 LDO, with 10µF input and output decoupling capacitors.
- **MCU Filtering & Decoupling:** Global 100nF/10µF decoupling capacitors on all VDD/VSS pins, plus ferrite bead (FB1) LC filtering for VDDA/VREF+.
- **Clock & Reset:** 8MHz HSE Crystal oscillator with 22pF load capacitors; hardware reset button with 10kΩ pull-up and 100nF RC debounce filter.
- **Boot Management:** BOOT0 (Pin 60 / PB8) anchored to GND with a 10kΩ pull-down resistor for reliable Flash memory execution.
- **Debug SWD:** Tag-Connect TC2030 footprint (SWDIO on PA13, SWCLK on PA14, SWO on PB3, NRST).
- **Board Identification (HWID):** 4-bit digital ID (PC0–PC3) with 10kΩ pull-downs + Analog ID (PA0) resistive divider (R6/R7).
- **Chainable Expansion Headers (J4/J5):** 4-pin male/female connectors carrying +5V pass-through power and I2C2 bus (SDA on PA8, SCL on PA9 with 4.7kΩ pull-ups to +3.3V).
- **16-pin Board-to-Board Connector (J2):** 2x8 header routing native SPI1 / PWM, I2C2, 3x TRT_GPIO, 4-bit HWID, and power rails.

## Pinout for Carrier

Pin 1 (GND)
Pin 2 (SPI_CS / PWM): PA4
Pin 3 (+5V)
Pin 4 (SPI_MOSI / PWM): PA7
Pin 5 (TRT_GPIO_1): PA1
Pin 6 (SPI_MISO / PWM): PA6
Pin 7 (+3.3V)
Pin 8 (SPI_SCK / PWM): PA5
Pin 9 (TRT_GPIO_2): PA2
Pin 10 (HWID_0): PC0
Pin 11 (SDA): PA8
Pin 12 (HWID_1): PC1
Pin 13 (SCL): PA9
Pin 14 (HWID_2): PC2
Pin 15 (TRT_GPIO_3): PA3
Pin 16 (HWID_3): PC3

Pin a2 (SPI_CS / PWM): PA4
Pin a4 (SPI_MOSI / PWM): PA7
Pin a6 (SPI_MISO / PWM): PA6
Pin a8 (SPI_SCK / PWM): PA5
Pin a10 (HWID_0): PC0
Pin a12 (HWID_1): PC1
Pin a14 (HWID_2): PC2
Pin a16 (HWID_3): PC3
Pin b2 (GND)
Pin b4 (+5V)
Pin b6 (TRT_GPIO_1): PA1
Pin b8 (+3.3V)
Pin b10 (TRT_GPIO_2): PA2
Pin b12 (SDA): PA8
Pin b14 (SCL): PA9
Pin b16 (TRT_GPIO_3): PA3