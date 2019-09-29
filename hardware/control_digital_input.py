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

    def IsOn(self)
        return automationhat.input[self.pin].is_on() == True
        self.last_action = "IS_ON"
        self.last_action_timestamp = datetime.datetime.now()

    def IsOff(self)
        return automationhat.input[self.pin].is_off() == True
        self.last_action = "IS_OFF"
        self.last_action_timestamp = datetime.datetime.now()



