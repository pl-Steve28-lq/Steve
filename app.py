from flask import Flask, render_template
import os
import urllib.request
import Wolfram
import matplotlib.pyplot as plt
from numpy import *
import base64
from random import random
import Plotter

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!'

@app.route('/des/<msg>')
def asdf(msg):
    return Wolfram.Wolframalpha(msg)

@app.route('/pic/<msg>')
def asdfer(msg):
    t = msg.split('^')
    v = t[0].split(' ');func = t[1]
    Plotter.Plotter(v, func)
    with open('images.txt', mode='rt', encoding='utf-8') as txt:
        a = txt.read().split(' ')[-2]
    img = a + ".png"
    return render_template('image.html', image_file=img)

@app.route('/info/<asdf>')
def i(asdf):
    return asdf

if __name__ == "__main__":
    app.run(host="192.168.219.105", port="5000")
