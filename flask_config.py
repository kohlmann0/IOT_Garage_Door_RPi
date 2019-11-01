import os

class FlaskConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this_is_the_default_secret_key'

