import json
import MockIo
# import control_digital_input
# import control_digital_output
# import control_relay

# This monitor specifically uses the RaspberryPi Zero W, with a Pimoroni AutomationPhat.
# It contains 3 digital inputs, 3 digital outputs, a relay and analog inputs.

class Monitor(object):
	
	def __init__(self, config, identifier):
		self.mock = config["mockIO"] == 'True'
		self.controls = dict
		for io_node in config["hardware"][identifier]["inputs"]:
			self.controls[io_node["id"]] = self.generate_control(input_node)


	def Run(self):
		print("RUNNING")
		

	# def State(self):
	# 	for control in self.controls:
	# 		state[control.id] = control.IsOn()
	# 	return state


	def generate_control(self, io_node, mock):
		if mock == True:
			return mockIo(io_node["id"], io_node)	

		if io_node["type"] == "input_digital":
			return control_digital_input(io_node["id"], io_node)
		elif io_node["type"] == "input_analog":
			raise Exception('input_analog control type has not been implemented yet.')
		elif io_node["type"] == "output_digital":
			return control_digital_output(io_node["id"], io_node)
		elif io_node["type"] == "output_relay":
			return control_relay(io_node["id"], io_node)
		else:
			raise Exception('Control type was not recognized:' + io_node["type"])



	# def validate_configuration(config)
		

	# while True:
	# 	isUp = automationhat.input[limit_switch_up].read()
	# 	isDown = automationhat.input[limit_switch_down].read()
		


	# 	print(isUp,isDown)
	# 	time.sleep(1)

