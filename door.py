from machine import Pin, PWM
from dcmotor import DCMotor


class door:
    door_switch = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)
    door_led = Pin(2, mode=Pin.OUT)
    door_switch_prv_state = 0
    door_message = "Open"

    def __init__(self, switch_pin=14, led_pin=2):
        self.door_switch = Pin(switch_pin, mode=Pin.IN, pull=Pin.PULL_UP)
        self.door_led = Pin(led_pin, mode=Pin.OUT)
        self.door_led.value(not self.door_switch.value())
        self.door_switch_prv_state = False
        self.get_doorState()  # call to make sure the start up state is correct

    def get_doorState(self):
        # this simplifies having an if on the LED
        self.door_led.value(not self.door_switch.value())
        # set our current state to the switch value
        logic_state = self.door_switch.value()
       # print(logic_state)
        if logic_state == 1 and self.door_switch_prv_state is False:
            self.door_message = "Open"
            self.door_switch_prv_state = True
        elif logic_state == 0 and self.door_switch_prv_state is True:
            self.door_message = "Closed"
            self.door_switch_prv_state = False
        return self.door_message
