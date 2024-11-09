# flask documentation
# https://flask.palletsprojects.com/en/2.0.x/

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/buy")
def buy():
    return "buy"

@app.route("/sell")
def sell():
    return "sell"

@app.route("/settings")
def settings():
    return "settings"

# save file

# run server on linux terminal
# cd to app dir
# export FLASK_APP=tutorial_part_6_flask_hello_world
# flask run

# run server on windows command line
# cd to app dir
# pip install flask # install globally
# set FLASK_APP=tutorial_part_6_flask_hello_world
# python -m flask run

# run server on powershell
# cd to app dir
# set FLASK_APP=tutorial_part_6_flask_hello_world
# set FLASK_ENV=development
# $env:FLASK_APP = "tutorial_part_6_flask_hello_world.py"
# flask run