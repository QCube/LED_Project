import time
import os

os.system("i2cset -y 1 0x49 0x00 0x00")
os.system("i2cset -y 1 0x49 0x01 0x04")

time.sleep(1)

def zoom(z):
    x = 0
    y = 0
    while y < z:
        while x < 16:
            time.sleep(0.02)
            os.system("i2cset -y 1 0x49 0x09 " + hex(x) )
            os.system("i2cset -y 1 0x49 0x0d " + hex(x) )
            os.system("i2cset -y 1 0x49 0x11 " + hex(x) )
            x = x + 1
        while x > 0:
            x = x - 1
            time.sleep(0.02)
            os.system("i2cset -y 1 0x49 0x09 " + hex(x) )
            os.system("i2cset -y 1 0x49 0x0d " + hex(x) )
            os.system("i2cset -y 1 0x49 0x11 " + hex(x) )
        y = y + 1

def flash(z):
    x = 0
    y = 0
    while y < z:
        time.sleep(0.02)
        if x == 0:
            os.system("i2cset -y 1 0x49 0x09 0x0f")
            os.system("i2cset -y 1 0x49 0x0d 0x0f")
            os.system("i2cset -y 1 0x49 0x11 0x0f")
            x = 1
        if x == 1:
            os.system("i2cset -y 1 0x49 0x09 0x00")
            os.system("i2cset -y 1 0x49 0x0d 0x00")
            os.system("i2cset -y 1 0x49 0x11 0x00")
            x = 0
	y = y + 1

def rainbow(z):
    reps = 0
    value = 0
    x = 0

    while reps < z:
        run = 1
        while run <= 3:
            if run == 1:
                register_Next = 9   # +1  0  0
                register_Last = 17  #  0  0 -1
            if run == 2:
                register_Next = 13  #  0 +1  0
                register_Last = 9   # -1  0  0
            if run == 3:
                register_Next = 17  #  0  0 +1
                register_Last = 13  #  0 -1  0
            
            while value < 16:
                time.sleep(0.05)
                os.system("i2cset -y 1 0x49 " + hex(register_Next) + " " + hex(value))
                os.system("i2cset -y 1 0x49 " + hex(register_Last) + " " + hex(15 - value))
                value += 1
            
            value = 0
            run += 1
        reps += 1
#zoom(10)
#flash(30)
rainbow(5)

os.system("i2cset -y 1 0x49 0x09 " + hex(0) )
os.system("i2cset -y 1 0x49 0x0d " + hex(0) )
os.system("i2cset -y 1 0x49 0x11 " + hex(0) )

