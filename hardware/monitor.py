import json
import time
import datetime
import collections

# 1. If on the raspberry Pi use the actual AutomationHat Library and hardware
# 2. If using Python3, try using the MockIO Import
# 3. If using Python2, try using the same thing, but with a relative path.
# https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x
try:
    import automationhat
    print("Real Hardware Loaded")
except ImportError:
    # TODO: log that we couldn't find the hardware and are instead using the MockIO
	try:
		from MockIo import automationhat
		print("MockIo1 Loaded")
	except ImportError:
		# from .MockIo import MockIO as automationhat
		import hardware.MockIo as automationhat
		print("MockIo2 Loaded")



# This monitor specifically uses the RaspberryPi Zero W, with a Pimoroni AutomationPhat.
# It contains 3 digital inputs, 3 digital outputs, a relay and analog inputs.

class Monitor(object):
	
	def __init__(self, config, identifier):
		self.controls = {}
		if "inputs" in config["hardware"][identifier]:
			for io_node in config["hardware"][identifier]["inputs"]:
				self.controls[io_node["id"]] = self.generate_control(io_node)

		if "outputs" in config["hardware"][identifier]:
			for io_node in config["hardware"][identifier]["outputs"]:
				self.controls[io_node["id"]] = self.generate_control(io_node)

	def generate_control(self, io_node):
		if io_node["type"] == "input_digital":
			return Control_Digital_Input(io_node["id"], io_node)
		elif io_node["type"] == "input_analog":
			raise Exception('input_analog control type has not been implemented yet.')
		elif io_node["type"] == "output_digital":
			return Control_Digital_Output(io_node["id"], io_node)
		elif io_node["type"] == "output_relay":
			return Control_Relay(io_node["id"], io_node)
		else:
			raise Exception('Control type was not recognized:' + io_node["type"])


	def Run(self):
		print("RUNNING")
		print("State:")
		for control in self.controls:
			print(self.controls[control].IsOn())



class Control_Digital_Input(object):

	def __init__(self, control_id, config):
		self.id = control_id
		self.pin = config["pin"] - 1
		self.last_action = "INIT"
		self.last_action_timestamp = datetime.datetime.now()
		self.Validate_Configuration()

	def IsOn(self):
		self.last_action = "IS_ON"
		self.last_action_timestamp = datetime.datetime.now()
		return automationhat.input[self.pin].is_on() == True


	def IsOff(self):
		self.last_action = "IS_OFF"
		self.last_action_timestamp = datetime.datetime.now()
		return automationhat.input[self.pin].is_off() == True


	def Validate_Configuration(self):
		if self.pin < 0 or self.pin > 2:
			raise Exception('The digital input for ' + self.id + ' is misconfigured (pin number = ' + (self.pin + 1) + '). Pin Number must be between 1 and 3.')




class Control_Digital_Output(object):

    def __init__(self, control_id, config):
        self.id = control_id
        self.pin = config["pin"] - 1
        self.last_action = "INIT"
        self.last_action_timestamp = datetime.datetime.now()
        self._validate_Configuration()

    def On(self):
        automationhat.output[self.pin].on()
        self.last_action = "ON"
        self.last_action_timestamp = datetime.datetime.now()

    def Off(self):
        automationhat.output[self.pin].off()
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
        return automationhat.output[self.pin].is_on() == True

    def IsOff(self):
        self.last_action = "IS_OFF"
        self.last_action_timestamp = datetime.datetime.now()
        return automationhat.output[self.pin].is_off() == True


    def _validate_Configuration(self):
        if self.pin < 0 or self.pin > 2:
            raise Exception('The digital output for ' + self.id + ' is misconfigured (pin number = ' + (self.pin + 1) + '). Pin Number must be between 1 and 3.')



class Control_Relay(object):

    def __init__(self, control_id, config):
        self.id = control_id
        self.pin = config["pin"] - 1
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



