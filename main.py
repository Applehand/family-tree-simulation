from src.game import run_test
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return run_test()
