
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

marker = "*"
def sierpinski(n):
    d = [marker]
    for i in xrange(n):
        sp = " " * (2 ** i)
        d = [sp+x+sp for x in d] + [x+" "+x for x in d]
    return d


canvas = Window(Vec2(255,255))
y = 0
x = 0
for line in sierpinski(7):
    y += 1
    for char in line:
        x += 1
        if char in marker:
            canvas.setColor(Vec2(x,y),Color.RED)
    x=0
canvas.refresh()
print "done"
