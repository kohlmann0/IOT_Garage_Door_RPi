# This is an attempt to Mock the hardware when we are not on a Raspberry Pi, and the AutomationHat is not available.

class automationhat(object):

	def __init__(self, control_id, config):        
		self.input = dict
		self.output = dict
		self.relay = dict

		self.input[0] = fakeInput()
		self.input[1] = fakeInput()
		self.input[2] = fakeInput()
		
		self.output[0] = fakeOutput()
		self.output[1] = fakeOutput()
		self.output[2] = fakeOutput()
		
		self.relay[0] = fakeRelay()
		self.relay[1] = fakeRelay()
		self.relay[2] = fakeRelay()



class fakeInput(object):
	def __init__(self):        
		self.state = False

	def is_on(self):
		return self.state == True		

	def is_off(self):
		return self.state == False
		
	def mockSet(self, value)
		self.state = value
		


class fakeOutput(object):
	def __init__(self):        
		self.state = False

	def is_on(self):
		return self.state == True		

	def is_off(self):
		return self.state == False

	def on(self):
		self.state == True
		
	def off(self):
		self.state == False
		
		
		
class fakeRelay(object):
	def __init__(self):        
		self.state = False

	def is_on(self):
		return self.state == True		

	def is_off(self):
		return self.state == False

	def on(self):
		self.state == True
		
	def off(self):
		self.state == False
		
		
