

"""
Class based state machine implementation

For insight to the state machine read:  https://learn.adafruit.com/circuitpython-101-state-machines/using-classes
pylint code debugging has not been implemented yet

March 24, 2022: The code is transitioning between all states using active-low button inputs on digital pins D5 & D6
    - no pull-up resistors needed, implemented in the 'Setup hardware' section
    - If you set "Testing = True" below, the code will report some of the internal print statments to help understand the transitions
"""

# pylint: disable=global-statement,stop-iteration-return,no-self-use,useless-super-delegation

import time
import board
import  digitalio
import busio
import adafruit_pcf8523
#import audioio
#import pwmio
from adafruit_debouncer import Debouncer

# Set to false to disable testing/tracing code
TESTING = False


# Implementation dependant things to tweak

# Pins

SWITCH_1_PIN = board.D5
SWITCH_2_PIN = board.D6

################################################################################
# Setup hardware


#i2c = busio.I2C(board.SCL, board.SDA)
#rtc = adafruit_ds3231.DS3231(i2c)

switch_1_io = digitalio.DigitalInOut(SWITCH_1_PIN)
switch_1_io.direction = digitalio.Direction.INPUT
switch_1_io.pull = digitalio.Pull.UP
switch_1 = Debouncer(switch_1_io)

switch_2_io = digitalio.DigitalInOut(SWITCH_2_PIN)
switch_2_io.direction = digitalio.Direction.INPUT
switch_2_io.pull = digitalio.Pull.UP
switch_2 = Debouncer(switch_2_io)


# Set the time for code testing
# Once finished testing, the time can be set using the REPL using similar code
if TESTING:
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2018,  12,   31,   23,  58,  55,    1,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    print("Setting time to:", t)
    #rtc.datetime = t
    #print()

################################################################################
# Global Variables

# Insert variables for time stamps


################################################################################
# Support functions

#  Code tracing Function
def log(s):
    """Print the argument if testing/tracing is enabled."""
    if TESTING:
        print(s)


################################################################################
# State Machine, Manages states

class StateMachine(object):

    def __init__(self):                             # Needed constructor
        self.state = None
        self.states = {}


    def add_state(self, state):                     # "add state" attribute, adds states to the machine
        self.states[state.name] = state

    def go_to_state(self, state_name):              # "go to state" attribute, facilittes transition to other states. Prints confirmation when "Testing = True"
        if self.state:
            log('Exiting %s' % (self.state.name))
            self.state.exit(self)
        self.state = self.states[state_name]
        log('Entering %s' % (self.state.name))
        self.state.enter(self)

    def pressed(self):                              # "button pressed" attribute. Accessed at the end of each loop, applies a pause and prints confirmaiton if setup.
        if self.state:
            log('Updating %s' % (self.state.name))
            self.state.pressed(self)
            #print("'StateMachine' Class occurrence")  # Use this print statement to understand how the states transition here to update the state in the serial monitor
            time.sleep(.5)                             # Critial pause needed to prevent the serial monitor from being "flooded" with data and crashing



################################################################################
# States

# Abstract parent state class: I'm not 100% sure that this state is the "parent class" for the states below.
# So far "StateMachine" appears to be the parent class, some clarification is needed to indentify how a class is called by "super().__init__()" (aka "Inheritance")

class State(object):

    def __init__(self):         # Constructor. Sets variables for the class, in this instance only, "self". Note machine variable below in the "enter" attribute
        pass

    @property
    def name(self):             # Attribute. Only the name is returned in states below. The State object shouldn't be called and returns nothing
        return ''

    def enter(self, machine):   # Class Attribute. Does what is commanded when the state is entered
        pass

    def exit(self, machine):    # Class Attribute. Does what is commanded when exiting the state
        pass

    def pressed(self, machine): # Class Attribute. Does what is commanded when a button is pressed
        print("'State' Class occurrence")   #This hasn't been called yet, I used this as a test to investigate the "inheritance" of child classes below.

########################################
# This state is active when powered on and other states return here
class Home(State):

    def __init__(self):
        super().__init__()          # Child class inheritance

    @property
    def name(self):
        return 'Home'

    def enter(self, machine):
        State.enter(self, machine)
        # Display a screen for the "Home" State, or enable a pin that displays the "Home" screen
        print('#### Home State ####')
        print('Placeholder to display the home screen on Epaper')
        print('Placeholder to display date and time\n')

    def exit(self, machine):
        State.exit(self, machine)

    def pressed(self, machine):
        if switch_1.fell:                                         #
            machine.go_to_state('Profile 1')
        if switch_2.fell:
            machine.go_to_state('Profile 2')
    # Experiment clearing the screen before transitioning, perhaps load the next screen here? OR in "exit"

########################################
# The "Profile 1" state. Either choose to track a task or use a focus timer.
class Profile1(State):

    def __init__(self):
        super().__init__()


    @property
    def name(self):
        return 'Profile 1'

    def enter(self, machine):
        State.enter(self, machine)
        print('#### Profile 1 State ####')
        print('Placeholder to display Profile 1 Screen')
        print('Placeholder to display date and time\n')

    def exit(self, machine):
        State.exit(self, machine)


    def pressed(self, machine):
        if switch_1.fell:
            machine.go_to_state('Tracking1')
        if switch_2.fell:
            machine.go_to_state('Focus Timer 1')
    # Experiment clearing the screen before transitioning, perhaps load the next screen here? OR in "exit"

########################################
# The "Tracking 1" state. Begin tracking task 1 in this state
class Tracking1(State):

    def __init__(self):
        super().__init__()


    @property
    def name(self):
        return 'Tracking1'

    def enter(self, machine):
        State.enter(self, machine)
        print('#### Tracking Task 1 State ####')
        print('Placeholder to display Tracking Task 1 Screen')
        print('Placeholder to display date and time')
        print('Placeholder to display counter for tracked time')
        print('Placeholder to store a time-stamp for a tracking START time (global variable)\n')

    def exit(self, machine):
        State.exit(self, machine)
        # Experiment clearing the Epaper Screen in this 'exit' attribute

    def pressed(self, machine):
        if switch_1.fell:                                         #Insert a switch #2 case, pull high or low to disable
            machine.go_to_state('Voice Note')
            print('Placeholder to tore a time-stamp for a tracking END time (global variable)\n')

########################################
# The "Focus Timer 1" state. Begin the focus timer here
class FocusTimer1(State):

    def __init__(self):
        super().__init__()


    @property
    def name(self):
        return 'Focus Timer 1'


    def enter(self, machine):
        State.enter(self, machine)
        print('#### Focus Timer 1 State ####')
        print('Placeholder to display Focus Timer 1 Screen')
        print('Display Focus Timer counting down')
        print('Display date and time\n')
        # Display a screen for "Focus Timer 1" state, or enable a pin that displays the "Focus Timer 1" screen

    def exit(self, machine):
        State.exit(self, machine)


    def pressed(self, machine):
        if switch_1.fell:                   # Either button press results in a transition to the "Home" state
            machine.go_to_state('Home')
        if switch_2.fell:                   # Question: Perhaps a transition to "Profile1" is more appropriate?
            machine.go_to_state('Home')
    # Experiment clearing the screen before transitioning, perhaps load the next screen here? OR in "exit"

########################################
# The "Profile 2" state. Implement at a later date. Any button press in this state causes a transition to the "Home" state.
class Profile2(State):

    def __init__(self):
        super().__init__()


    @property
    def name(self):
        return 'Profile 2'

    def enter(self, machine):
        State.enter(self, machine)
        print('#### Profile 2 State ####')
        print('Placeholder to display Profile 2 Screen')
        print('Placeholder to display Profile 2 Screen, date and time\n')

    def exit(self, machine):
        State.exit(self, machine)


    def pressed(self, machine):
        if switch_1.fell:
            machine.go_to_state('Home')     # Either button press returns to "Home" state, further profiles will be implemented in the future
        if switch_2.fell:
            machine.go_to_state('Home')
    # Experiment clearing the screen before transitioning, perhaps load the next screen here? OR in "exit"

########################################
# The "Voice Note" state. A placeholder state that has an option to record a voice note or return to the "home" state
class VoiceNote(State):

    def __init__(self):
        super().__init__()


    @property
    def name(self):
        return 'Voice Note'

    def enter(self, machine):
        State.enter(self, machine)
        print('#### Voice Note State ####')
        print('Placeholder to display Voice Note Screen')
        print('Placeholder to display, "Yes or No" to record a note\n')


    def exit(self, machine):
        State.exit(self, machine)


    def pressed(self, machine):
        if switch_1.fell:                   # Yes button results in a transition to the "Record" state
            machine.go_to_state('Record')
        if switch_2.fell:                   # No button results in a transition to the "Home" state
            machine.go_to_state('Home')
    # Experiment clearing the screen before transitioning, perhaps load the next screen here? OR in "exit"

########################################
# The "Record Note" state. A placeholder state that will record a note then transition to the "home" state
# Constains an easter egg photo of Professor Levine on vacation
class Record(State):

    def __init__(self):
        super().__init__()


    @property
    def name(self):
        return 'Record'

    def enter(self, machine):
        State.enter(self, machine)
        print('#### Record Note State ####')
        print('Placeholder to display Prof. Levine on vacation Screen')                       # Easter egg
        print('Placeholder to display, "Placeholder for second semester functionality!"\n')

    def exit(self, machine):
        State.exit(self, machine)
        print('Log date, start time stamp, end time stamp and voice note to .csv\n')    # Upon exit, log the global variables containing time stamps to the SD Card

    def pressed(self, machine):

        if switch_1.fell:
            print('Placeholder to display "Ah Ah Ah" screen\n')                             # Easter egg
            machine.go_to_state('Home')                                                     # Return "Home"
        if switch_2.fell:
            machine.go_to_state('Home')                                                     # Return "Home"



################################################################################
# Create the state machine

LTB_state_machine = StateMachine()          # Defines the state machine
LTB_state_machine.add_state(Home())         # Adds the listed states to the machine (Except for the class, "State"
LTB_state_machine.add_state(Profile1())
LTB_state_machine.add_state(Tracking1())
LTB_state_machine.add_state(FocusTimer1())
LTB_state_machine.add_state(Profile2())
LTB_state_machine.add_state(VoiceNote())
LTB_state_machine.add_state(Record())

LTB_state_machine.go_to_state('Home')   #Starts the state machine in the "Home" state

while True:
    switch_1.update()               #Checks the switch 1 state each time the loop executes, necessary for button state changes
    switch_2.update()               #Checks the switch 1 state each time the loop executes, necessary for button state changes
    LTB_state_machine.pressed()     #Transitions to the StateMachine attrubute, "pressed". Doesn't do much there other than report the current state
