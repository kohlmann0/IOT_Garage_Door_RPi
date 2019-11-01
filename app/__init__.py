from flask import Flask
from flask_config import FlaskConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)

from app import routes

