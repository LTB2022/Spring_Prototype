# LTB Main Demo Code for the E-Paper Display
# Author: Micah Hernandez
# Date: 2022.08.25

# import required Python libraries
import sys

# library directories
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic/2in9')
fontdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import time
from datetime import date
import logging
from PIL import Image, ImageDraw, ImageFont
import traceback
import threading

# get touch screen display library
from TP_lib import INCT_Dev_Touch_LTB

# get e-paper display library
from TP_lib import E-Paper_Driver_2in9_LTB

logging.basicConfig(level=logging.DEBUG)
flag_t = 1

def pthread_irq() :
    print("pthread irq running")
    while flag_t == 1 :
        if(tp.digital_read(tp.INT) == 0) :
            ICNT_Dev.Touch = 1
        else :
            ICNT_Dev.Touch = 0
        time.sleep(0.01)
    print("thread irq: exit")




try:
    logging.info("E-Paper_Driver_2in9_LTB Touch Demo")

    # initialize the display and touch drivers
    epd = E-Paper_Driver_2in9_LTB.EPD_2IN9_V2()
    tp = INCT_Dev_Touch_LTB.INCT86()

    ICNT_Dev = INCT_Dev_Touch_LTB.ICNT_Development()
    ICNT_Old = INCT_Dev_Touch_LTB.ICNT_Development()

    # clear display, 0 = black, 0xFF = white
    logging.info("init and Clear")
    epd.init()
    tp.ICNT_Init()
    epd.Clear(0xFF)

    # top date bar, global, stays visible through all screens



    # write buffer contents to display
    epd.display_Base(epd.getbuffer(image))

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    flag_t = 0
    epd.sleep()
    time.sleep(2)
    t1.join()
    epd.Dev_exit()
    exit()# Write your code here :-)
