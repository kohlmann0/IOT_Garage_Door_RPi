import time
import datetime

class MockIo(object):

	def __init__(self, control_id, config):        
		self.id = control_id
		self.title = config["title"]
		self.pin = -1
		self.last_action = "INIT"
		self.last_action_timestamp = datetime.datetime.now()
		self.state = True

	def On(self):
		self.state = True

	def Off(self):
		self.state = False

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
		return self.state == True

	def IsOff(self):
		return self.state == False
