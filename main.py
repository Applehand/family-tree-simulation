from flask import Flask, render_template, send_file
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/test")
def test():
    file_path = os.path.join(app.root_path, 'test.json')
    return send_file(file_path)
