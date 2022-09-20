# /*****************************************************************************
# * | File        :	  EPD_Config_LTB.py
# * | Author      :   Waveshare team
# * | Function    :   Hardware underlying interface
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2020-12-21
# * | Info        :


import RPi.GPIO as GPIO
import time
from smbus import SMBus
import spidev
import ctypes
import logging

# e-Paper
EPD_RST_PIN     = 17
EPD_DC_PIN      = 25
EPD_CS_PIN      = 8
EPD_BUSY_PIN    = 24

# TP
TRST    = 22
INT     = 27

spi     = spidev.SpiDev(0, 0)
address = 0x0
# address = 0x14
# address = 0x48
bus     = SMBus(1)

def digital_write(pin, value):
    GPIO.output(pin, value)

def digital_read(pin):
    return GPIO.input(pin)

def delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_writebyte(data):
    spi.writebytes(data)

def spi_writebyte2(data):
    spi.writebytes2(data)

def i2c_writebyte(reg, value):
    bus.write_word_data(address, (reg>>8) & 0xff, (reg & 0xff) | ((value & 0xff) << 8))

def i2c_write(reg):
    bus.write_byte_data(address, (reg>>8) & 0xff, reg & 0xff)

def i2c_readbyte(reg, len):
    i2c_write(reg)
    rbuf = []
    for i in range(len):
        rbuf.append(int(bus.read_byte(address)))
    return rbuf

def module_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(EPD_RST_PIN, GPIO.OUT)
    GPIO.setup(EPD_DC_PIN, GPIO.OUT)
    GPIO.setup(EPD_CS_PIN, GPIO.OUT)
    GPIO.setup(EPD_BUSY_PIN, GPIO.IN)

    GPIO.setup(TRST, GPIO.OUT)
    GPIO.setup(INT, GPIO.IN)

    spi.max_speed_hz = 10000000
    spi.mode = 0b00

    return 0

def module_exit():
    logging.debug("spi end")
    spi.close()
    bus.close()

    logging.debug("close 5V, Module enters 0 power consumption ...")
    GPIO.output(EPD_RST_PIN, 0)
    GPIO.output(EPD_DC_PIN, 0)
    GPIO.output(EPD_CS_PIN, 0)

    GPIO.output(TRST, 0)

    GPIO.cleanup()


### END OF FILE #### Write your code here :-)
