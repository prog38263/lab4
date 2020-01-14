import os
import socket

from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)


@app.route('/')
def hello():
    return "Hello World from Python in a Flask app in a Docker container"
