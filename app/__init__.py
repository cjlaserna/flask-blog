import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/kristen')
def kristen():
    return render_template('kristen.html', title="MLH Fellow - Kristen", url=os.getenv("URL"))

@app.route('/helen')
def helen():
    return render_template('helen.html', title="MLH Fellow - Helen", url=os.getenv("URL"))

@app.route('/catherine')
def catherine():
    return render_template('catherine.html', title="MLH Fellow - Catherine", url=os.getenv("URL"))
