import Window
import Pixel
import java.awt.Color as Color
import Vec2
import random
import math

import PixelMathAbstractionInterface

class PixelMathBridge(PixelMathAbstractionInterface):
    def getPixelQuickly(self, id, x, y):
        return pmGetPixelQuickly(int(id),int(x),int(y))
    def setPixelQuickly(self, id, x, y, color):
        return pmSetPixelQuickly(int(id), int(x), int(y), color)

    def openImage(self, id, filename):
        return pmOpenImage(int(id), filename)
    def newImage(self, id, title, width, height, r, g, b):
        return pmNewImage(id, title, int(width), int(height), int(r), int(g), int(b))

    def getImageWidth(self, id):
        return pmGetImageWidth(int(id))
    def getImageHeight(self, id):
        return pmGetImageHeight(int(id))

    def refresh(self, id):
        return pmUpdateDisplay(int(id))
Window.init(PixelMathBridge())

def inBounds(bounds, position):
    return position.x <= bounds.x and position.y <= bounds.y

size = Vec2(500.0,500.0)
middle = size.scaled(0.5)
canvas = Window(size)

others = []
for pixel in canvas.pixels():
    bright = random.randrange(0,255)
    pixel.setColor(Color(bright,bright,bright))
canvas.refresh()

for i in range(2,50,2):
    new = pmNewImage(i, str(i), int(size.x), int(size.y), 255,0,0)
    others.append(new)
    pmSetSource1(canvas.id)
    pmSetDestination(new)
    newRelSize = int(min(size.y,size.x)/i)
    offset = random.randrange(0,min(size.x,size.y)-newRelSize)
    pmSetFormula("s1(x/"+str(i)+"+"+str(offset)+",y/"+str(i)+"+"+str(offset)+")")
    pmCompute()

final = Window(size)
for pixel in final.pixels():
    pos = pixel.position
    value = 0
    for window in others:
        value += pmGetPixel(window, int(pos.x), int(pos.y))[0]
    value /= len(others)
    value = int(value)
    pixel.setColor(Color(value,value,value))
final.refresh()

canvas.refresh()
print "done"

