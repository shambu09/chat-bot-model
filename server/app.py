from flask import Flask

from model import load_model, find_similiar
from log import Logger
from utils import read_ans, read_qs, write_ans, write_qs

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'