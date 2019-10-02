import os
import time
import json
# import automationhat
# import logging
# import logging.handlers
import hardware.monitor



if __name__ == '__main__':
    # syslog.openlog('garage')

    config_file = open('config.json')
    config = json.load(config_file)    
    monitor = monitor(config, "garage_door")
    # site = Site(config, monitor)

    config_file.close
    monitor.Run()
