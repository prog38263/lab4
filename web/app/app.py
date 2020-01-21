import os
import socket
from flask import Flask
from flask import render_template, flash
from redis import Redis
from app.forms import SimpleForm

app = Flask(__name__,
        static_url_path='',
        static_folder='static',
        template_folder='templates')
app.config['SECRET_KEY'] = 'this-is-a-secret-key-you-generate-for-your-app'
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    return "Hello World from Python in a Flask app in a Docker container"

@app.route('/simpleform', methods=['GET','POST'])
def simple_form():
    sform = SimpleForm()
    if redis.get("hits") is None:
        redis.set("hits", 0)
    if sform.validate_on_submit():
        redis.incr("hits")
        flash(f"Hi {sform.username.data}")
    return render_template("simpleform.html", title="Simple Form", form=sform, hits=int(redis.get("hits")))

