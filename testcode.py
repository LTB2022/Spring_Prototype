import time
import busio
import board
import displayio
import terminalio
import digitalio
import adafruit_il0373
import adafruit_pcf8523
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label

# Creates object I2C that connects the I2C module to pins SCL and SDA
myI2C = busio.I2C(board.SCL, board.SDA)
# Creates an object that can access the RTC and communicate that information along using I2C.
rtc = adafruit_pcf8523.PCF8523(myI2C)

displayio.release_displays()

BLACK = 0x000000
WHITE = 0xFFFFFF

# This pinout works on a Feather M4 and may need to be altered for other boards.
spi = busio.SPI(board.SCK, board.MOSI)  # Uses SCK and MOSI
epd_cs = board.D9
epd_dc = board.D10

display_bus = displayio.FourWire(
    spi, command=epd_dc, chip_select=epd_cs, baudrate=1000000
)
time.sleep(1)

display = adafruit_il0373.IL0373(
    display_bus,
    width=296,
    height=128,
    rotation=270,
    black_bits_inverted=False,
    color_bits_inverted=False,
    grayscale=True,
    refresh_time=1,
)

# wait until we can draw
time.sleep(display.time_to_refresh)

# main group to hold everything
main_group = displayio.Group()

# white background. Scaled to save RAM
bg_bitmap = displayio.Bitmap(display.width // 8, display.height // 8, 1)
bg_palette = displayio.Palette(1)
bg_palette[0] = WHITE
bg_sprite = displayio.TileGrid(bg_bitmap, x=0, y=0, pixel_shader=bg_palette)
bg_group = displayio.Group(scale=8)
bg_group.append(bg_sprite)
main_group.append(bg_group)

font_file = "fonts/Helvetica-Bold-16.pcf"
FONT = bitmap_font.load_font(font_file)

# first example label
TEXT = "Task 1"
text_area= label.Label(
    FONT,
    text=TEXT,
    color=WHITE,
    background_color=0x666666,
    padding_top=3,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
)
text_area.x = 10
text_area.y = 14
main_group.append(text_area)

#set_time = time.struct_time((2022, 3, 16, 22, 59, 45, 4, -1, -1))
#print("Setting time to:", set_time)
#rtc.datetime = set_time

# Comment out the above four lines again after setting the time!


while True:
    current = rtc.datetime

    hour = current.tm_hour % 12
    if hour == 0:
        hour = 12

    am_pm = "AM"
    if current.tm_hour / 12 >= 1:
        am_pm = "PM"

    time_display = "{:d}:{:02d} {}".format(hour, current.tm_min, am_pm)


# second example label
clock = label.Label(
    FONT,
    scale=1,
    text=time_display,
    color=BLACK,
    background_color=0x999999,
    padding_top=3,
    padding_bottom=3,
    padding_right=4,
    padding_left=4,
)
# centered
clock.anchor_point = (0.5, 0.25)
clock.anchored_position = (display.width // 2, display.height // 2)
main_group.append(clock)

# show the main group and refresh.
display.show(main_group)
display.refresh()
while True:
    pass
