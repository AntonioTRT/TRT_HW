# STM32G474RET6 Carrier Board — Especificación Técnica Oficial

## 1. Descripción General

La **Carrier Board STM32G474** es una plataforma de desarrollo modular de alto rendimiento basada en el microcontrolador ARM Cortex-M4F **STM32G474RET6** (LQFP-64, hasta 170 MHz con FPU y DSP). Diseñada específicamente para fabricación y ensamblaje SMT en **JLCPCB**, utiliza encapsulados estándar fáciles de inspeccionar y soldar (**0805 pasivos, SOT-23, SOD-123 y LQFP-64**).

La tarjeta se interconecta con placas hijas (*daughterboards*) a través del conector Board-to-Board principal **J2 (2x8 pines, numeración estándar 1 a 16)**, integrando buses de comunicación (SPI1, I2C1 con gestión de energía), control de potencia (driver de motor PWM con MOSFET AO3400A) e identificación de hardware digital (HWID de 4 bits).

---

## 2. Especificaciones de Hardware

### 2.1. Alimentación y Regulación
- **Entrada Principal:** +5V nominal vía puerto **USB-C (J6)**. Cuenta con resistencias de pull-down de **5.1 kΩ** en las líneas `CC1` y `CC2` para compatibilidad completa con fuentes y cables USB-C a USB-C (Power Delivery Sink 5V/3A máx).
- **Regulador LDO:** **AMS1117-3.3** en encapsulado SOT-223, entregando un riel de +3.3V regulado (hasta 800 mA de pico / 1 A máx).
- **Filtrado y Desacoplo:**
  - Capacitores cerámicos (MLCC 0805) de **10 µF** en la entrada (+5V) y salida (+3.3V) del regulador.
  - Red de desacoplo distribuida en el MCU: **100 nF** en cada par `VDD`/`VSS` adyacente a los pines, complementados por un capacitor de carga de **10 µF**.
  - **Filtro Analógico:** Perla de ferrita (**FB1**) con capacitor de **100 nF** a masa para las líneas `VDDA` y `VREF+`, aislando el dominio analógico de ruidos digitales.
  - Pin `VBAT` unificado directamente al riel de **+3.3V**.

### 2.2. Reloj, Reset y Depuración
- **Oscilador Principal (HSE):** Cristal de cuarzo pasivo de **8.000 MHz** con capacitores de carga de **22 pF** a GND en `OSC_IN` (PF0) y `OSC_OUT` (PF1).
- **Circuito de Reset (NRST):** Pulsador táctil a GND con resistencia de pull-up de **10 kΩ** a +3.3V y capacitor cerámico de **100 nF** para supresión de rebotes mecánicos y transitorios.
- **Depuración SWD:** Huella estándar **Tag-Connect TC2030-NL / TC2030** que provee:
  - `SWDIO` en **PA13**
  - `SWCLK` en **PA14**
  - `SWO` en **PB3** (Asynchronous Trace)
  - `NRST` para hardware reset por depurador
  - `+3.3V` (VTref) y `GND`

### 2.3. Periféricos e Interfaces On-Board
- **Bus I2C1 con Gestión de Energía:**
  - `PB9` (SDA) y `PB8` (SCL).
  - Resistencias de Pull-Up de **2.2 kΩ** conectadas a un nodo conmutable controlado por el pin **PC15** (`I2C_PU_EN`).
  - Permite desconectar los pull-ups para apagar el bus en modos de bajo consumo (*Sleep/Stop*).
- **Bus SPI1:**
  - `PA5` (SCK), `PA6` (MISO), `PA7` (MOSI), `PB6` (CS).
- **Driver de Motor Low-Side (PWM):**
  - MOSFET canal N **AO3400A** (30V, 5.7A, $R_{DS(on)} < 35\text{ m}\Omega$ a 3.3V $V_{GS}$) en encapsulado SOT-23.
  - Controlado desde el pin **PB4** (Timer 3, Canal 1 / `TIM3_CH1`).
  - Red de compuerta: Resistencia de gate $R_G = 100\ \Omega$ y resistencia pull-down de seguridad $R_{PD} = 10\text{ k}\Omega$ a GND.
  - Protección inductiva: Diodo Schottky Flyback **1N5819HW** (SOD-123) en antiparalelo con la carga + capacitor cerámico de **100 nF** para amortiguación de EMI.
  - Conector de salida de motor **J1** (Paso 2.54 mm): Pin 1 = `+5V`, Pin 2 = `Drain del MOSFET`.
- **LEDs de Diagnóstico:**
  - `LED_PWR` (Verde): Polarizado a +3.3V mediante resistencia de **1 kΩ** ($I_F \approx 1.3\text{ mA}$).
  - `LED_USER` (Azul): Conectado al pin **PA5** (`SPI_SCK`) mediante resistencia de **470 Ω** (emula el `LED_BUILTIN` de Arduino Pin 13).

---

## 3. Conector Board-to-Board (J2 — 2x8 Pines, Numeración Estándar 1 a 16)

El conector principal **J2** utiliza una huella estándar de doble hilera (paso 2.00 mm / 2.54 mm) con numeración numérica consecutiva (Pines 1 al 16), organizada en fila impar (señales SPI / HWID) y fila par (alimentación / I2C / GPIOs):

### 3.1. Tabla de Mapeo Definitiva para J2

| Pin Físico J2 | Fila | Etiqueta de Red | Pin STM32G474 | Funciones Nativas STM32 | Equivalente Arduino | Descripción |
| :---: | :---: | :--- | :---: | :--- | :---: | :--- |
| **Pin 1** | Impar | `SPI_CS / PWM` | **PB6** | TIM4_CH1, TIM16_CH1N, USART1_TX | D10 / PWM | Chip Select SPI o PWM auxiliar |
| **Pin 2** | Par | `GND` | — | Riel de Masa común (0V) | GND | Masa de alimentación |
| **Pin 3** | Impar | `SPI_MOSI / PWM`| **PA7** | SPI1_MOSI, TIM3_CH2, TIM1_CH1N | D11 / PWM | Datos MOSI o salida PWM |
| **Pin 4** | Par | `+5V` | — | Riel de entrada USB VBUS | 5V | Alimentación de potencia principal |
| **Pin 5** | Impar | `SPI_MISO / PWM`| **PA6** | SPI1_MISO, TIM3_CH1, TIM16_CH1, ADC2_IN3 | D12 / PWM | Datos MISO o entrada ADC / PWM |
| **Pin 6** | Par | `TRT_GPIO_1` | **PA1** | TIM2_CH2, USART2_RTS, ADC1_IN2 | D2 / A4 | GPIO / Entrada Analógica / Timer |
| **Pin 7** | Impar | `SPI_SCK / PWM` | **PA5** | SPI1_SCK, TIM2_CH1, ADC2_IN2 | D13 / SCK | Reloj SPI / LED Builtin / PWM |
| **Pin 8** | Par | `+3.3V` | — | Salida del LDO AMS1117-3.3 | 3.3V | Lógica y alimentación de sensores |
| **Pin 9** | Impar | `HWID_0` | **PC0** | ADC1_IN6, ADC2_IN6, LPTIM1_IN1 | A0 | Identificación Hardware Bit 0 (ADC/Digital) |
| **Pin 10**| Par | `TRT_GPIO_2` | **PA4** | DAC1_OUT1, SPI1_NSS, ADC2_IN1 | A5 / DAC | GPIO / Salida Analógica Pura DAC |
| **Pin 11**| Impar | `HWID_1` | **PC1** | ADC1_IN7, ADC2_IN7, LPTIM1_OUT | A1 | Identificación Hardware Bit 1 (ADC/Digital) |
| **Pin 12**| Par | `SDA` | **PB9** | I2C1_SDA, TIM4_CH4, FDCAN1_TX | D14 / SDA | Datos I2C1 (Pull-up conmutable vía PC15) |
| **Pin 13**| Impar | `HWID_2` | **PC2** | ADC1_IN8, ADC2_IN8, LPTIM1_IN2 | A2 | Identificación Hardware Bit 2 (ADC/Digital) |
| **Pin 14**| Par | `SCL` | **PB8** | I2C1_SCL, TIM4_CH3, FDCAN1_RX | D15 / SCL | Reloj I2C1 (Compartido con BOOT0) |
| **Pin 15**| Impar | `HWID_3` | **PC3** | ADC1_IN9, ADC2_IN9, LPTIM1_ETR | A3 | Identificación Hardware Bit 3 (ADC/Digital) |
| **Pin 16**| Par | `TRT_GPIO_3` | **PB0** | TIM1_CH2N, TIM3_CH3, ADC1_IN15 | D3 / PWM | GPIO / PWM auxiliar / ADC |

---

### 3.2. Distribución Física de Pines en el Header (Vista Superior)

```text
               +-------------------+
SPI_CS   (PB6) | [ 1]         [ 2] | GND
SPI_MOSI (PA7) | [ 3]         [ 4] | +5V
SPI_MISO (PA6) | [ 5]         [ 6] | TRT_GPIO_1 (PA1)
SPI_SCK  (PA5) | [ 7]         [ 8] | +3.3V
HWID_0   (PC0) | [ 9]         [10] | TRT_GPIO_2 (PA4)
HWID_1   (PC1) | [11]         [12] | SDA        (PB9)
HWID_2   (PC2) | [13]         [14] | SCL        (PB8)
HWID_3   (PC3) | [15]         [16] | TRT_GPIO_3 (PB0)
               +-------------------+
                    Conector J2
```

---

## 4. Pines Internos y Periféricos Dedicados

| Función | Pin STM32G474 | Características |
| :--- | :--- | :--- |
| **Driver Motor (GATE)** | **PB4** | TIM3_CH1 (PWM Low-Side, MOSFET AO3400A a conector J1) |
| **Habilitador Pull-Up I2C**| **PC15** | Control digital de polarización para resistencias I2C1 (Push-Pull HIGH = ON, High-Z = OFF) |
| **LED Usuario (Azul)** | **PA5** | Compartido con SPI1_SCK (R=470Ω a GND) |
| **USB D-** | **PA11** | USB 2.0 Full Speed Data - |
| **USB D+** | **PA12** | USB 2.0 Full Speed Data + |
| **SWDIO** | **PA13** | Tag-Connect Pin 4 |
| **SWCLK** | **PA14** | Tag-Connect Pin 2 |
| **SWO** | **PB3** | Tag-Connect Pin 6 (Asynchronous SWO Trace) |

---

## 5. Guía de Integración de Firmware

### 5.1. Configuración de Option Bytes para PB8 / BOOT0
El microcontrolador **STM32G474RET6** multiplexa el pin físico 60 entre `PB8` y la señal de selección de arranque `BOOT0`.
- **Problema:** De fábrica, si `nBOOT0_SEL = 1`, en cada reinicio el hardware muestrea el pin PB8. Dado que PB8 está conectado a la línea I2C `SCL` con una resistencia de pull-up, el MCU detectará un nivel alto (`BOOT0 = 1`) y entrará en el bootloader DFU de ST en lugar de ejecutar la memoria Flash.
- **Solución Obligatoria:** Configurar el registro de Option Bytes `FLASH_OPTR`:
  - `nBOOT0_SEL = 0` (Bit 27): El valor de BOOT0 es ignorado desde el pin físico PB8 y se toma del bit de software `nBOOT0`.
  - `nBOOT0 = 1` (Bit 26): En lógica invertida, un valor de `1` equivale a `BOOT0 = 0`, forzando el arranque directo desde la **Flash Principal**.

#### Configuración por Software (HAL / Firmware):
```c
void Configure_Boot_OptionBytes(void) {
    FLASH_OBProgramInitTypeDef obInit = {0};
    
    HAL_FLASH_Unlock();
    HAL_FLASH_OB_Unlock();

    HAL_FLASHEx_OBGetConfig(&obInit);
    
    // Si nBOOT0_SEL está en 1 (muestreo por pin físico PB8), cambiar a software
    if ((obInit.UserConfig & FLASH_OPTR_nBOOT0_SEL) != 0) {
        obInit.OptionType = OPTIONBYTE_USER;
        obInit.UserType   = OB_USER_nBOOT0_SEL | OB_USER_nBOOT0;
        // nBOOT0_SEL = 0 (software), nBOOT0 = 1 (arranque en Flash)
        obInit.UserConfig = OB_nBOOT0_SEL_DISABLE | OB_nBOOT0_SET;
        
        HAL_FLASHEx_OBProgram(&obInit);
        HAL_FLASH_OB_Launch(); // Aplica cambios y reinicia el MCU
    }

    HAL_FLASH_OB_Lock();
    HAL_FLASH_Lock();
}
```

---

### 5.2. Control de Pull-Ups I2C vía PC15 (`I2C_PU_EN`)
Las resistencias de 2.2 kΩ están conectadas al pin **PC15**.

> [!WARNING]
> **Regla de Oro de Firmware para PC15:**
> - Para **ACTIVAR** el bus I2C: Configurar `PC15` como **Salida Push-Pull** en nivel **ALTO** (`GPIO_PIN_SET` = 3.3V).
> - Para **DESACTIVAR** el bus I2C: Configurar `PC15` como **Entrada Flotante (High-Z / No-Pull)**.
> - **NUNCA** configurar `PC15` como salida en nivel **BAJO** (`0V`), ya que esto forzaría a masa las líneas `SDA` y `SCL` mediante 2.2 kΩ, bloqueando la comunicación y consumiendo corriente innecesaria.

#### Implementación HAL:
```c
// Activa las resistencias de pull-up (Bus I2C operativo)
void I2C_Pullups_Enable(void) {
    GPIO_InitTypeDef GPIO_InitStruct = {0};
    __HAL_RCC_GPIOC_CLK_ENABLE();

    GPIO_InitStruct.Pin = GPIO_PIN_15;
    GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

    HAL_GPIO_WritePin(GPIOC, GPIO_PIN_15, GPIO_PIN_SET); // Alimenta +3.3V al nodo
}

// Desconecta las resistencias de pull-up (Modo bajo consumo)
void I2C_Pullups_Disable(void) {
    GPIO_InitTypeDef GPIO_InitStruct = {0};
    __HAL_RCC_GPIOC_CLK_ENABLE();

    // Configurar en entrada de alta impedancia (High-Z)
    GPIO_InitStruct.Pin = GPIO_PIN_15;
    GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);
}
```

---

### 5.3. Control del Driver de Motor PWM (PB4 / TIM3_CH1)
El MOSFET **AO3400A** es activado directamente por lógica de 3.3V desde `PB4`.

- **Frecuencia óptima recomendada:** 10 kHz a 20 kHz.
- Reloj APB1 (`TIM3CLK`) = 170 MHz.
  - `Prescaler = 16` $\rightarrow$ Frecuencia de conteo = 10 MHz.
  - `Period (ARR) = 999` $\rightarrow$ Frecuencia PWM = 10 kHz ($10\text{ MHz} / 1000$).
  - Resolución del ciclo de trabajo: 0 a 1000 (0% a 100%).

```c
// Iniciar señal PWM
HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_1);

// Modificar velocidad del motor (0 a 1000)
void Motor_SetSpeed(uint16_t speed) {
    if (speed > 1000) speed = 1000;
    __HAL_TIM_SET_COMPARE(&htim3, TIM_CHANNEL_1, speed);
}
```

---

## 6. Checklist Crítico para el Layout de PCB (JLCPCB)

1. **Ruta de Retorno y Bucles de Potencia del Motor (J1 / AO3400A / D1):**
   - El bucle cerrado formado por `J1 Pin 1 (+5V)` $\rightarrow$ `Motor` $\rightarrow$ `J1 Pin 2` $\rightarrow$ `Diodo 1N5819HW` debe colocarse **lo más compacto posible** para minimizar la radiación EMI.
   - Pistas de potencia entre `J1`, el Drain del MOSFET y el Source a `GND` con un ancho mínimo de **1.2 mm a 1.5 mm** (o polígono de cobre).
   - Colocar el Source del MOSFET directamente a la masa general mediante múltiples vías a plano de masa para evitar ruido por rebote de masa (*ground bounce*).
2. **Ubicación de Condensadores de Desacoplo del MCU:**
   - Cada condensador de **100 nF** debe colocarse inmediatamente adyacente a su respectivo pin `VDD`, conectando primero el pad del capacitor antes de la vía hacia el plano interno.
   - La perla de ferrita `FB1` y su capacitor de 100 nF para `VDDA`/`VREF+` deben ubicarse pegados a los pines 18 y 19.
3. **Oscilador de Cristal HSE de 8 MHz (PF0 / PF1):**
   - Trazar pistas cortas y simétricas entre el cristal y los pines del MCU.
   - Colocar un anillo de guarda de masa (`GND guard ring`) alrededor del cristal y sus capacitores de 22 pF.
   - No rutear señales digitales de alta velocidad (como PWM o SPI) por debajo del oscilador.
4. **Par Diferencial USB (PA11 / PA12):**
   - Impedancia diferencial de **90 Ω**. Ruteo en paralelo con separación constante y longitudes simétricas acopladas.
   - Mantener el plano de masa continuo por debajo sin cortes.