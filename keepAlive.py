from flask import Flask
from threading import Thread
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "I'm alive!"


def run():
    #app.run(host='0.0.0.0', port=8080)   Use this if you want to run on testing on replit
    os.system("gunicorn -b 0.0.0.0:8080 keepAlive:app --log-file -")


def keep_alive():
    t = Thread(target=run)
    t.start()
