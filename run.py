from flask import Flask
import main


app = Flask(__name__)


def scrap():
    return 'hi sasan'