import os
import time
import json
# import logging
# import logging.handlers
import hardware.monitor as H



if __name__ == '__main__':
	# syslog.openlog('garage')

	config_file = open('config.json')
	config = json.load(config_file)    
	monitor_garagedoor = H.Monitor(config, "garage_door")
	# monitor_manDoor = H.Monitor(config, "man_door")	
	monitor_powerdown = H.Monitor(config, "raspberry_pi_power_off")

	# site = Site(config, monitor)

	config_file.close
	monitor_garagedoor.Run()
	monitor_powerdown.Run()
