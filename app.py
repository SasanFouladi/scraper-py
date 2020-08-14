from flask import Flask
import main


app = Flask(__name__)


@app.route('/')
def run():
    return 'hi sasan'