from flask import render_template
from app import app

import json
import time
import datetime
import subprocess

# Hardware setup
import hardware.monitor as H
import hardware.listen_for_shutdown as L

monitors = {}

# Init
# if __name__ == '__main__':
config_file = open('config.json')
config = json.load(config_file)   
config_file.close
monitors["garage_door"] = H.Monitor(config, "garage_door")
monitors["raspberry_pi_power_off"] =  H.Monitor(config, "raspberry_pi_power_off")
for monitor in monitors:
    monitors[monitor].Run()
	

@app.route('/')
@app.route('/index')
def index():
    #Set this to false before you deploy
    debug = True 
    user = {'username': 'TEST'}
    return render_template('index.html', title='Garage Door Monitor', debug=debug, user=user, monitors=monitors)

def push_closer_button():
    monitors["garage_door"].controls["opener_switch"].Pulse_On(1)

def push_power_button():
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
    