import os

def chip_init():
    os.system("i2cset -y 1 0x49 0x00 0x00")
    os.system("i2cset -y 1 0x49 0x01 0x04")

def on():
    RED.on()
    GREEN.on()
    BLUE.on()

def off():
    RED.off()
    GREEN.off()
    BLUE.off()

class LED():
    def __init__(self, i2c_adress):
        self.value = 0
        self.saver = 0
        self.i2c_adress = i2c_adress

    def write(self, value):
        self.value = value
        os.system("i2cset -y 1 " + self.i2c_adress + " " + str(value))

    def on(self):
        self.write(self.saver)

    def off(self):
        if self.value > 0:
            self.saver = self.value
            self.write(0)

    def toggle(self):
        if self.value > 0:
            self.saver = self.value
            self.write(0)
        else:
            self.write(self.saver)

    def inc(self):
        if self.value < 15:
            self.value += 1
            self.write(self.value)

    def dec(self):
        if self.value > 0:
            self.value -= 1
            self.write(self.value)


chip_init()

RED = LED("0x49 0x09")
GREEN = LED("0x49 0x0d")
BLUE = LED("0x49 0x11")

if __name__ == "__main__":
    chip_init()
    RED = LED("0x49 0x09")
    GREEN = LED("0x49 0x0d")
    BLUE = LED("0x49 0x11")