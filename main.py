import os
import sys
from flask import Flask, render_template, send_file
from dotenv import load_dotenv

load_dotenv()

project_path = os.getenv('PROJECTPATH')
sys.path.append(project_path)

# app = Flask(__name__)

# @app.route("/")
# def base():
#     return render_template('base.html')

# @app.route("/test")
# def test():
#     return 'Test'

from src.game import test

test()

