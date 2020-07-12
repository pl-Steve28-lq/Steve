import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy import *
from random import random

def Plotter(xlist, func):
    plt.clf()
    x = arange(int(xlist[0]), int(xlist[1]), 0.01*(int(xlist[1])-int(xlist[0])))
    y = eval(func)
    t = str(random()*(10**9)).replace(".","_")
    plt.plot(x,y)
    plt.savefig('./static/{}.png'.format(t), dpi=300)
    with open('images.txt', mode='at', encoding='utf-8') as txt:
        txt.write('{} '.format(t))
