import automationhat
import time
import datetime

class Control_Digital_Input(object):

	def __init__(self, control_id, config):        
		self.id = control_id
		self.title = config["title"]
		self.pin = config["pin_number"] - 1
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
			raise Exception('The digital input for ' + self.title + ' is misconfigured (pin number = ' + (self.pin + 1) + '). Pin Number must be between 1 and 3.')



