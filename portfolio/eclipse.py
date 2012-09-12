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

def normal(input):
    return int(min(255,max(0,input)))

size = Vec2(500.0,500.0)
middle = size.scaled(0.5)
canvas = Window(size)

clipse = middle.plus(50,0)

for pixel in canvas.pixels():
    pos = pixel.position
    
    bright = normal(random.random()*255)
    bright /= 10

    outer = 110
    inner = 100
    dist = pos.distance(middle)
    if dist < outer:
        if(dist<inner):
            bright = 0
        else:
            b = normal((outer-dist)*8+ bright)
            bright = b
   
    pixel.setColor(Color(bright, bright, bright))

def drawStar(position, bright, size):
    bright = normal(bright*255)
    canvas.setColor(position, Color(bright,bright,bright))

for i in range(500):
    position = Vec2(random.randrange(0, size.x), random.randrange(0, size.y))
    if position.distance(middle) > 100:
        drawStar(position,0.5,1)
canvas.refresh()
print "done"

