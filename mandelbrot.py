import Window
import Pixel
import java.awt.Color as Color
import Vec2
import System

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


size = Vec2(600,600)
canvas = Window(size)

def inMandelbrotSet(c):
    z = 0
    h = 0
    for h in xrange(0, 100):
        z = z**2 + c
        if abs(z) > 2:
            break;
    if abs(z) >= 2:
        return -1
    else:
        return h

for x in range (0, size.x):
    real = x / 200.0 - 1.5
    for y in range(0, size.y):
        img = y / 200.0 -1.5
        c = complex(real, img)

        n = inMandelbrotSet(c)
        if n!= -1:
            #print n/100.0
            canvas.setColor(Vec2(x,y), Color.getHSBColor(n/100.0,1,0.5))
canvas.refresh()
print "done"

