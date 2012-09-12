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

size = Vec2(500.0,500.0)
middle = size.scaled(0.5)
canvas = Window(size)

for pixel in canvas.pixels():
    brightness = random.random()
    brightness *= min(1,(middle.distance(pixel.position)/(max(middle.x,middle.y))))
    brightness /= 10

    pixel.setColor(Color((int)(brightness*255),(int)(brightness*255),(int)(brightness*255)))
canvas.refresh()


pmSetPolar()
pmSetDestination(canvas.id)

pmSetFormula("if rho < (sin(theta*100)+1)*75 or rho < 100 then RGB(source1(rho,theta)/2,0,0) else source1(rho, theta)")
pmCompute()



print "done"

