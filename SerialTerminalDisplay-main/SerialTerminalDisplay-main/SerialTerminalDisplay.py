import time
import board
import displayio
import terminalio
import busio
from adafruit_display_text import label
import adafruit_il0373

displayio.release_displays()

# This pinout works on a Feather M4 and may need to be altered for other boards.
spi = busio.SPI(board.SCK, board.MOSI)  # Uses SCK and MOSI
epd_cs = board.D9
epd_dc = board.D10

#FourWire is an SPI based display bus.
#We make it because the display must be connected to the host controller using a "display bus".
display_bus = displayio.FourWire(
    spi, command=epd_dc, chip_select=epd_cs, baudrate=1000000
)
time.sleep(1)

# We don't have a built in display, so we have to use the adafruit_il0373 driver
# built-in display
#display = board.DISPLAY

#Notice how this display we have made is an instance of the driver.
#It takes the display bus we made as the first input.
#A display can only show a group.
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

# A group is the display context.

main_group = displayio.Group()
#A display is cabable of "showing" one display group at a time.
display.show(main_group)

# create the label
updating_label = label.Label(
    font=terminalio.FONT, text="Time Is:\n{}".format(time.monotonic()), scale=2
)

# set label position on the display
updating_label.anchor_point = (0, 0)
updating_label.anchored_position = (20, 20)

# add label to group that is showing on display
# Note that groups can have items inserted or appended.
main_group.append(updating_label)

# Main loop
while True:

    # update text property to change the text showing on the display
    #ATTENTION: This is where we see the error in the main module of this code.
    updating_label.text = "Time Is:\n{}".format(time.monotonic())
    time.sleep(5)