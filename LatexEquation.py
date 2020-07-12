from urllib.request import urlretrieve
from random import random
from PIL import Image


def Ltx(eq):
    u = str(random()*(10**9)).replace(".", "_")
    eq1 = eq.replace(" ", "%20")
    url = 'https://latex.codecogs.com/gif.latex?%5CLARGE%20{}'.format(eq1)
    urlretrieve(url, 'static/{}.png'.format(u))

    tx = Image.open('./static/{}.png'.format(u))
    w, h = tx.size
    if w > 210:
        url = 'https://latex.codecogs.com/gif.latex?{}'.format(eq1)
        urlretrieve(url, 'static/2{}.png'.format(u))
        ty = Image.open('./static/2{}.png'.format(u))
        W, H = ty.size
        bg1 = Image.new('RGB', (W+20, H+20), (255, 255, 255))
        bg1.paste(ty, (10, 10))
        bg1.save('./static/3{}.png'.format(u))
        with open('images.txt', mode='at', encoding='utf-8') as txt:
            txt.write('{} 2{} 3{} '.format(u, u, u))
    else:
        bg = Image.new('RGB', (w+20, h+20), (255, 255, 255))
        bg.paste(tx, (10, 10))
        bg.save('./static/1{}.png'.format(u))
        with open('images.txt', mode='at', encoding='utf-8') as txt:
            txt.write('{} 1{} '.format(u, u))
