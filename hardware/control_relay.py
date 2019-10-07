import time
import datetime

# 1. If on the raspberry Pi use the actual AutomationHat Library and hardware
# 2. If using Python3, try using the MockIO Import
# 3. If using Python2, try using the same thing, but with a relative path.
# https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x
try:
    import automationhat
except ImportError:
    # TODO: log that we couldn't find the hardware and are instead using the MockIO
	try:
		from MockIo import automationhat
	except ImportError:
		from .MockIo import automationhat


class Control_Relay(object):

    def __init__(self, control_id, config):
        self.id = control_id
        self.title = config["title"]
        self.pin = config["pin_number"] - 1
        self.last_action = "INIT"
        self.last_action_timestamp = datetime.datetime.now()

    def On(self):
        automationhat.relay[self.pin].on()
        self.last_action = "ON"
        self.last_action_timestamp = datetime.datetime.now()

    def Off(self):
        automationhat.relay[self.pin].off()
        self.last_action = "OFF"
        self.last_action_timestamp = datetime.datetime.now()

    def Pulse_On(self, time_seconds):
        self.On()
        time.sleep(time_seconds)
        self.Off()
        self.last_action = "PULSE_ON"
        self.last_action_timestamp = datetime.datetime.now()

    def Pulse_off(self, time_seconds):
        self.Off()
        time.sleep(time_seconds)
        self.On()
        self.last_action = "PULSE_OFF"
        self.last_action_timestamp = datetime.datetime.now()

    def IsOn(self):
        self.last_action = "IS_ON"
        self.last_action_timestamp = datetime.datetime.now()
        return automationhat.relay[self.pin].is_on() == True
        
    def IsOff(self):
        self.last_action = "IS_OFF"
        self.last_action_timestamp = datetime.datetime.now()
        return automationhat.relay[self.pin].is_off() == True
        



