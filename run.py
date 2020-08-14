from flask import Flask
import main


app = Flask(__name__)


def hello():
    return 'hi sasan'