import Window
import Pixel
import java.awt.Color as Color
import Vec2

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



canvas = Window(Vec2(600,600))

def inMandelbrotSet(c):
    z = 0
    for h in xrange(0, 20):
        z = z**2 + c
        if abs(z) > 2:
            break;
    if abs(z) > = 2:
        return False
    else:
        return True

for x in range (0, 600):
    real = x / 200.0 - 1.5
    for y in range(0, 600):
        img = y / 200.0 -1.5
        c = complex(real, img)
        if mandel(c):
            canvas.setColor(Vec2(x,y), Color.RED)
print "done"
