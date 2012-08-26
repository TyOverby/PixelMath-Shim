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


# Start Code
def inCarpet(x, y):
    while True:
        if x == 0 or y ==0:
            return True
        elif x%3 == 1 and y%3 == 1:
            return False

        x /= 3
        y /= 3


canvas = Window(Vec2(3**5,3**5))

def carpet(n):
    for x in xrange(3**n):
        for y in xrange(3**n):
            if inCarpet(x, y):
                canvas.setColor(Vec2(x,y),Color.RED)
    canvas.refresh()

carpet(5)
print "done"

