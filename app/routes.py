from flask import render_template, flash, redirect
from app import app
from app import forms

import json
import time
import datetime
import subprocess

# Hardware setup
from hardware import monitor as H
from hardware import listen_for_shutdown as L

monitors = {}

# Init Hardware Monitor
# if __name__ == '__main__':
config_file = open('hardware_config.json')
config = json.load(config_file)
config_file.close
monitors["garage_door"] = H.Monitor(config, "garage_door")
monitors["raspberry_pi_power_off"] =  H.Monitor(config, "raspberry_pi_power_off")
for monitor in monitors:
    monitors[monitor].Run()


# View Controls and Routes
@app.route('/')
@app.route('/index')
def index():
    #Set this to false before you deploy
    debug = True
    state = 'TEST'
    user = {'username': 'TEST'}
    return render_template('index.html', title='Garage Door Monitor', debug=debug, user=user, monitors=monitors)


@app.route('/login', methods=['GET','POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title="Log In", form=form)


#Monitor Functions
def push_closer_button():
#    monitors["garage_door"].controls["opener_switch"].Pulse_On(1)
    print("Push_Closer_Button was Pressed")


def push_power_button():
#    subprocess.call(['shutdown', '-h', 'now'], shell=False)
    print("Push_Power_Button was Pressed")
