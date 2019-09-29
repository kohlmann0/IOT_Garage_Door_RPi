import os
import time
import json
import automationhat

scriptDirectory = os.path.dirname(os.path.abspath('__file__'))
print scriptDirectory

with open(os.path.join(scriptDirectory, 'config.json')) as json_file:
	config = json.load(json_file)
	print('limit_switch_up = Input:', config['garage']['limit_switch_up'])
	print('limit_switch_down = Input:', config['garage']['limit_switch_down'])
	print('push_button_opener = Output:', config['garage']['push_button_opener'])

	limit_switch_up = config['garage']['limit_switch_up']-1
	limit_switch_down = config['garage']['limit_switch_down']-1
	push_button_opener = config['garage']['push_button_opener']-1

	if limit_switch_up < 0 or limit_switch_up > 2:
		raise Exception('Upper Limit Switch is not configured properly. Pin Number must be between 1 and 3. Set to ', limit_switch_up)

	if limit_switch_down < 0 or limit_switch_down > 2:
		raise Exception('Lower Limit Switch is not configured properly. Pin Number must be between 1 and 3. Set to ', limit_switch_up)

	if push_button_opener < 0 or push_button_opener > 2:
		raise Exception('Open push button is not configured properly. Pin Number must be between 1 and 3. Set to ', limit_switch_up)

	if limit_switch_up == limit_switch_down:
		raise Exception('Upper and Lower Limit Switchs are not configured properly. Pin Number must be different. Set to ', limit_switch_up, ',', limit_switch_down)



while True:
	isUp = automationhat.input[limit_switch_up].read()
	isDown = automationhat.input[limit_switch_down].read()
	


	print(isUp,isDown)
	time.sleep(1)
