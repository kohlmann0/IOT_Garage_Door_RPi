# This is an attempt to Mock the hardware when we are not on a Raspberry Pi, and the AutomationHat is not available.

class fakeInput(object):
	def __init__(self):        
		self.state = False

	def is_on(self):
		return self.state == True		

	def is_off(self):
		return self.state == False
		
	def mockSet(self, value):
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
		
		

input = {}
output = {}
relay = {}
input[0] = fakeInput()
input[1] = fakeInput()
input[2] = fakeInput()		
output[0] = fakeOutput()
output[1] = fakeOutput()
output[2] = fakeOutput()		
relay[0] = fakeRelay()
relay[1] = fakeRelay()
relay[2] = fakeRelay()