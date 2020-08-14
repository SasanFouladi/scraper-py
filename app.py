from flask import Flask
import main


app = Flask('app')


@app.route('/')
def app():
    return 'hi sasan'