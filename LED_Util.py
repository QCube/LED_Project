import LED_I2C_Interface as Interface

RED = Interface.LED("0x49 0x09")
GREEN = Interface.LED("0x49 0x0d")
BLUE = Interface.LED("0x49 0x11")

def on():
    RED.on()
    GREEN.on()
    BLUE.on()

def off():
    RED.off()
    GREEN.off()
    BLUE.off()
