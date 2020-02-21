import pyautogui as ui
from collections import Counter
import operator
from time import sleep
from PIL import Image
import os
def getPixel(clr,diap,count):
    im = ui.screenshot().convert('RGB')
    pixel = im.load()
    size = im.size
    touch = 0
    print(count)
    for x in range(size[0]):
        for y in range(size[1]):
            if clr[0]+diap>=pixel[x,y][0]>=clr[0]-diap and clr[1]+diap>=pixel[x,y][1]>=clr[1]-diap and clr[2]+diap>=pixel[x,y][2]>=clr[2]-diap:
                touch+=1
                if touch == count:
                    return x, y
    return None
def getCountPixels(screen, bg):
    im = Image.open('vid/'+bg).convert('RGB')
    im = list(set(im.getdata()))
    im22 = Image.open('vid/'+screen).convert('RGB')
    im2 = im22.getdata()
    im3 = []
    for i in im2:
        if i in im:
            continue
        else:
            im3.append(i)
    return dict(Counter(im3))
PersPixel = getCountPixels('001.jpg','000.png')
color = max(PersPixel.items(), key=operator.itemgetter(1))[0]
while True:
    sleep(2)
    pos = getPixel(color,5,PersPixel[color])
    if not (pos is None):
        x,y = pos
        ui.moveTo(x=x,y=y,duration=0.2)
