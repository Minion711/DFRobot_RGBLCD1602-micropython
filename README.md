Adaptation of the arduino library of https://github.com/DFRobot/DFRobot_RGBLCD1602?tab=readme-ov-file

# 🧭 DFRobot RGB1602 MicroPython Driver (ESP32 Compatible)

MicroPython library for controlling the **DFRobot 16x2 RGB LCD** (V1 and V2) via **I²C** on ESP32 or Raspberry Pi Pico.  
Supports **automatic RGB register mapping** depending on the module version (V1 → `0x60`, V2 → `0x2D`).

---

## ✨ Features

- ✅ Compatible with both **V1** and **V2** DFRobot RGB1602 displays  
- ✅ Works on **ESP32**, **ESP8266**, and **Raspberry Pi Pico**  
- ✅ Automatic detection of RGB register mapping  
- ✅ Simple API for text and color control  
- ✅ Clean MicroPython code (no external dependencies)

---

## 🧰 Wiring

| LCD Pin | Description | ESP32 Pin |
|----------|--------------|-----------|
| VCC      | +5V-3v3      | 5V-3v3    |
| GND      | Ground       | GND       |
| SDA      | I²C Data     | GPIO 21   |
| SCL      | I²C Clock    | GPIO 22   |

---

## ⚙️ I²C Addresses

| Version | LCD Address | RGB Address |
|----------|--------------|-------------|
| V1       | `0x3E`       | `0x60`      |
| V2       | `0x3E`       | `0x2D`      |

---

## 🚀 Usage Example

```python
from machine import I2C, Pin
from DFRobot_RGB1602 import DFRobot_RGB1602
import time

# Initialize I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

# Create display instance
lcd = DFRobot_RGB1602(i2c, lcd_addr=0x3E, rgb_addr=0x2D)  # or 0x60 for V1

# Set backlight color
lcd.set_rgb(255, 0, 0)  # Red
time.sleep(1)
lcd.set_rgb(0, 255, 0)  # Green
time.sleep(1)
lcd.set_rgb(0, 0, 255)  # Blue

# Print text
lcd.clear()
lcd.print("Hello DFRobot!")
lcd.set_cursor(0, 1)
lcd.print("MicroPython OK")


Done with the help of chatGPT tested with ESP32 in thonny 
