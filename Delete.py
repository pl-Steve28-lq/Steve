import os

def Delete():
    try:
        with open('images.txt') as imgs:
            r = imgs.read().split()
            for i in r:
                os.remove("./static/" + i + ".png")
        with open('images.txt', mode='w+t') as img:
            img.write("")
    except:
        pass
