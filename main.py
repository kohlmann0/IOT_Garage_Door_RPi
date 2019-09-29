import os
import time
import json
import automationhat



if __name__ == '__main__':
    syslog.openlog('garage')

    config_file = open 'config.json'
    config = json.load(config_file)
    monitor = Monitor(config)
    site = Site(config, monitor)

    config_file.close
    monitor.run()
