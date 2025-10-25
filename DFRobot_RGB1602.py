from machine import I2C, Pin
import time
patate = 0

class DFRobot_RGB1602:
    def __init__(self, i2c, lcd_addr=0x3E, rgb_addr=0x2D):
        self.i2c = i2c
        self.lcd_addr = lcd_addr
        self.rgb_addr = rgb_addr

        # Mapping RGB selon l'adresse du module
        if rgb_addr == 0x2D:  # v2
            self.rgb_regs = (0x01, 0x02, 0x03)  # R, G, B
        elif rgb_addr == 0x60:  # v1
            self.rgb_regs = (0x04, 0x02, 0x03)  # R, G, B v1
        else:
            self.rgb_regs = (0x01, 0x02, 0x03)  # fallback

        time.sleep_ms(200)
        self._init_lcd()
        time.sleep_ms(100)
        self._init_rgb()

    # --- LCD ---
    def _write_cmd(self, cmd):
        self.i2c.writeto(self.lcd_addr, bytes([0x80, cmd]))
        time.sleep_ms(2)

    def _write_data(self, data):
        self.i2c.writeto(self.lcd_addr, bytes([0x40, data]))

    def _init_lcd(self):
        time.sleep_ms(50)
        self._write_cmd(0x38)
        self._write_cmd(0x39)
        self._write_cmd(0x14)
        self._write_cmd(0x70)
        self._write_cmd(0x56)
        self._write_cmd(0x6C)
        time.sleep_ms(200)
        self._write_cmd(0x38)
        self._write_cmd(0x0C)
        self._write_cmd(0x01)
        time.sleep_ms(2)

    def clear(self):
        self._write_cmd(0x01)
        time.sleep_ms(2)

    def set_cursor(self, col, row):
        row_offsets = [0x00, 0x40]
        self._write_cmd(0x80 | (col + row_offsets[row]))

    def print(self, text):
        text = str(text)  # conversion automatique
        for c in text:
            self._write_data(ord(c))


    # --- RGB ---
    def _set_reg(self, reg, data):
        self.i2c.writeto_mem(self.rgb_addr, reg, bytes([data]))

    def _init_rgb(self):
        self._set_reg(0x00, 0x00)
        self._set_reg(0x01, 0x00)
        self._set_reg(0x08, 0xAA)

    def set_rgb(self, r, g, b):
        # utilise automatiquement le mapping selon le module
        regs = self.rgb_regs
        self._set_reg(regs[0], r)
        self._set_reg(regs[1], g)
        self._set_reg(regs[2], b)
