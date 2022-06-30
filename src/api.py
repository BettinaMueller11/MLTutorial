from flask import Flask, Response, request
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return{"hello": "world"}
