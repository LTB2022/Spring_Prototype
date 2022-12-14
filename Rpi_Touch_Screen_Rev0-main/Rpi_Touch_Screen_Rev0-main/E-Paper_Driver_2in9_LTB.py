
import logging
from . import EPD_Config_LTB
import numpy as np

# Display resolution
EPD_WIDTH       = 128
EPD_HEIGHT      = 296

class EPD_2IN9_V2:
    def __init__(self):
        self.reset_pin = EPD_Config_LTB.EPD_RST_PIN
        self.dc_pin = EPD_Config_LTB.EPD_DC_PIN
        self.busy_pin = EPD_Config_LTB.EPD_BUSY_PIN
        self.cs_pin = EPD_Config_LTB.EPD_CS_PIN
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT
      EPD_Config_LTB.address = 0x48

    WF_PARTIAL_2IN9 = [
        0x0,0x40,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x80,0x80,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x40,0x40,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x80,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0A,0x0,0x0,0x0,0x0,0x0,0x0,
        0x1,0x0,0x0,0x0,0x0,0x0,0x0,
        0x1,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x0,0x0,0x0,0x0,0x0,0x0,0x0,
        0x22,0x22,0x22,0x22,0x22,0x22,0x0,0x0,0x0,
        0x22,0x17,0x41,0xB0,0x32,0x36,
    ]

    WF_PARTIAL_2IN9_Wait = [
    0x0,0x40,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x80,0x80,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x40,0x40,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x80,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0A,0x0,0x0,0x0,0x0,0x0,0x2,
    0x1,0x0,0x0,0x0,0x0,0x0,0x0,
    0x1,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x0,0x0,0x0,0x0,0x0,0x0,0x0,
    0x22,0x22,0x22,0x22,0x22,0x22,0x0,0x0,0x0,
    0x22,0x17,0x41,0xB0,0x32,0x36,
    ]

    # Hardware reset
    def reset(self):
        EPD_Config_LTB.digital_write(self.reset_pin, 1)
        EPD_Config_LTB.delay_ms(20)
        EPD_Config_LTB.digital_write(self.reset_pin, 0)
        EPD_Config_LTB.delay_ms(2)
        EPD_Config_LTB.digital_write(self.reset_pin, 1)
        EPD_Config_LTB.delay_ms(20)

    def send_command(self, command):
        EPD_Config_LTB.digital_write(self.dc_pin, 0)
        EPD_Config_LTB.digital_write(self.cs_pin, 0)
        EPD_Config_LTB.spi_writebyte([command])
        EPD_Config_LTB.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        EPD_Config_LTB.digital_write(self.dc_pin, 1)
        EPD_Config_LTB.digital_write(self.cs_pin, 0)
        EPD_Config_LTB.spi_writebyte([data])
        EPD_Config_LTB.digital_write(self.cs_pin, 1)

    def send_data2(self, data):
        EPD_Config_LTB.digital_write(self.dc_pin, 1)
        EPD_Config_LTB.digital_write(self.cs_pin, 0)
        EPD_Config_LTB.spi_writebyte2(data)
        EPD_Config_LTB.digital_write(self.cs_pin, 1)

    def ReadBusy(self):
        # logging.debug("e-Paper busy")
        while(EPD_Config_LTB.digital_read(self.busy_pin) == 1):      #  0: idle, 1: busy
            EPD_Config_LTB.delay_ms(0.1)
        # logging.debug("e-Paper busy release")

    def TurnOnDisplay(self):
        self.send_command(0x22) # DISPLAY_UPDATE_CONTROL_2
        self.send_data(0xF7)
        self.send_command(0x20) # MASTER_ACTIVATION
        self.ReadBusy()

    def TurnOnDisplay_Partial(self):
        self.send_command(0x22) # DISPLAY_UPDATE_CONTROL_2
        self.send_data(0x0F)
        self.send_command(0x20) # MASTER_ACTIVATION
        # self.ReadBusy()

    def TurnOnDisplay_Partial_Wait(self):
        self.send_command(0x22) # DISPLAY_UPDATE_CONTROL_2
        self.send_data(0x0F)
        self.send_command(0x20) # MASTER_ACTIVATION
        self.ReadBusy()

    def SendLut(self, lut):
        self.send_command(0x32)
        # for i in range(0, 153):
            # self.send_data(self.WF_PARTIAL_2IN9[i])
        if(lut):
            self.send_data2(self.WF_PARTIAL_2IN9)
        else:
            self.send_data2(self.WF_PARTIAL_2IN9_Wait)
        self.ReadBusy()

    def SetWindow(self, x_start, y_start, x_end, y_end):
        self.send_command(0x44) # SET_RAM_X_ADDRESS_START_END_POSITION
        # x point must be the multiple of 8 or the last 3 bits will be ignored
        self.send_data((x_start>>3) & 0xFF)
        self.send_data((x_end>>3) & 0xFF)
        self.send_command(0x45) # SET_RAM_Y_ADDRESS_START_END_POSITION
        self.send_data(y_start & 0xFF)
        self.send_data((y_start >> 8) & 0xFF)
        self.send_data(y_end & 0xFF)
        self.send_data((y_end >> 8) & 0xFF)

    def SetCursor(self, x, y):
        self.send_command(0x4E) # SET_RAM_X_ADDRESS_COUNTER
        # x point must be the multiple of 8 or the last 3 bits will be ignored
        self.send_data(x & 0xFF)

        self.send_command(0x4F) # SET_RAM_Y_ADDRESS_COUNTER
        self.send_data(y & 0xFF)
        self.send_data((y >> 8) & 0xFF)
        self.ReadBusy()

    def init(self):
        if (EPD_Config_LTB.module_init() != 0):
            return -1
        # EPD hardware init start
        self.reset()

        self.ReadBusy();
        self.send_command(0x12);  #SWRESET
        self.ReadBusy();

        self.send_command(0x01); #Driver output control
        self.send_data(0x27);
        self.send_data(0x01);
        self.send_data(0x00);

        self.send_command(0x11); #data entry mode
        self.send_data(0x03);

        self.SetWindow(0, 0, self.width-1, self.height-1);

        self.send_command(0x21); #  Display update control
        self.send_data(0x00);
        self.send_data(0x80);	

        self.SetCursor(0, 0);
        self.ReadBusy();
        # EPD hardware init end
        return 0

    def getbuffer(self, image):
        # logging.debug("bufsiz = ",int(self.width/8) * self.height)
        buf = [0xFF] * (int(self.width/8) * self.height)
        image_monocolor = image.convert('1')
        imwidth, imheight = image_monocolor.size
        pixels = image_monocolor.load()
        # logging.debug("imwidth = %d, imheight = %d",imwidth,imheight)
        if(imwidth == self.width and imheight == self.height):
            # logging.debug("Vertical")
            for y in range(imheight):
                for x in range(imwidth):
                    # Set the bits for the column of pixels at the current position.
                    if pixels[x, y] == 0:
                        buf[int((x + y * self.width) / 8)] &= ~(0x80 >> (x % 8))
        elif(imwidth == self.height and imheight == self.width):
            # logging.debug("Horizontal")
            for y in range(imheight):
                for x in range(imwidth):
                    newx = y
                    newy = self.height - x - 1
                    if pixels[x, y] == 0:
                        buf[int((newx + newy*self.width) / 8)] &= ~(0x80 >> (y % 8))
        return buf

    def display(self, image):
        if (image == None):
            return
        self.send_command(0x24) # WRITE_RAM
        # for j in range(0, self.height):
            # for i in range(0, int(self.width / 8)):
                # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)
        self.TurnOnDisplay()

    def display_Base(self, image):
        if (image == None):
            return

        self.send_command(0x24) # WRITE_RAM
        # for j in range(0, self.height):
            # for i in range(0, int(self.width / 8)):
                # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.send_command(0x26) # WRITE_RAM
        # for j in range(0, self.height):
            # for i in range(0, int(self.width / 8)):
                # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.TurnOnDisplay()

    def display_Partial(self, image):
        if (image == None):
            return

        # EPD_Config_LTB.digital_write(self.reset_pin, 0)
        # EPD_Config_LTB.delay_ms(2)
        # EPD_Config_LTB.digital_write(self.reset_pin, 1)
        # EPD_Config_LTB.delay_ms(2)

        self.SendLut(1);
        self.send_command(0x37);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);  	
        self.send_data(0x40);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);

        self.send_command(0x3C); #BorderWavefrom
        self.send_data(0x80);

        self.send_command(0x22);
        self.send_data(0xC0);
        self.send_command(0x20);
        self.ReadBusy();

        self.SetWindow(0, 0, self.width - 1, self.height - 1)
        self.SetCursor(0, 0)

        self.send_command(0x24) # WRITE_RAM
        # for j in range(0, self.height):
            # for i in range(0, int(self.width / 8)):
                # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.TurnOnDisplay_Partial()

    def display_Partial_Wait(self, image):
        if (image == None):
            return

        EPD_Config_LTB.digital_write(self.reset_pin, 0)
        EPD_Config_LTB.delay_ms(1)
        EPD_Config_LTB.digital_write(self.reset_pin, 1)
        # EPD_Config_LTB.delay_ms(2)

        self.SendLut(0);
        self.send_command(0x37);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);  	
        self.send_data(0x40);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);
        self.send_data(0x00);

        self.send_command(0x3C); #BorderWavefrom
        self.send_data(0x80);

        self.send_command(0x22);
        self.send_data(0xC0);
        self.send_command(0x20);
        self.ReadBusy();

        self.SetWindow(0, 0, self.width - 1, self.height - 1)
        self.SetCursor(0, 0)

        self.send_command(0x24) # WRITE_RAM
        # for j in range(0, self.height):
            # for i in range(0, int(self.width / 8)):
                # self.send_data(image[i + j * int(self.width / 8)])
        self.send_data2(image)

        self.TurnOnDisplay_Partial_Wait()

    def Clear(self, color):
        self.send_command(0x24) # WRITE_RAM
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(color)
        self.TurnOnDisplay()

    def sleep(self):
        self.send_command(0x10) # DEEP_SLEEP_MODE
        self.send_data(0x01)

    def Dev_exit(self):
        EPD_Config_LTB.module_exit()
### END OF FILE #### Write your code here :-)
