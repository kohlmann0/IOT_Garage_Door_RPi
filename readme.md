This is a monitor system for a garage door.
It includes a hardware controller and a web portal


# Hardware #
* [RaspberryPi Zero W](https://www.adafruit.com/product/2885)
* [Pimoroni AutomationPhat](https://www.adafruit.com/product/3352)
* [Magnetic contact switch x2](https://www.adafruit.com/product/375)


# Required Python modules #
* [AutomationHat Library](https://github.com/pimoroni/automation-hat)
* [Flask](https://github.com/pimoroni/automation-hat)
* [python-dotenv](https://pypi.org/project/python-dotenv/) (optional)


# Electrical connections #
AutomationPi Digital Input 1 - Door up limit switch
AutomationPi Digital Input 2 - Door down limit switch
AutomationPi Digital Input 3 - Power down Raspberry Pi
AutomationPi Relay Output 1 - Door closer switch



# TODO: #
1. EagleCAD wiring diagram
2. Configurable website - Remove hard-coded values
3. Componentize website (React? But might need to be flask-wtf webforms though)
4. Website security
5. Push-notifications to authorized users (app notifications, sms, ?)
6. Access Logging and logview on website
