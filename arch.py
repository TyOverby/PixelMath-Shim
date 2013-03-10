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

size = Vec2(100,100)
canvas = Window(size)
pmOpenImage(canvas.id,"archery.jpg")


def neighboring(position):
    yield position.plus(Vec2(-1,-1))
    yield position.plus(Vec2(-1,0))
    yield position.plus(Vec2(-1,1))
    yield position.plus(Vec2(0,-1))
    #yield position.plus(Vec2(0,0))
    yield position.plus(Vec2(0,1))
    yield position.plus(Vec2(1,-1))
    yield position.plus(Vec2(1,0))
    yield position.plus(Vec2(1,1))

for pos in canvas.positions():
    for neighbor in neighboring(pos):
        if neighbor.y < size.y and neighbor.x < size.x and neighbor.y >0 and neighbor.x >0:
            current = canvas.getColor(pos)
            next    = canvas.getColor(neighbor)
            if current.equals(next):
                canvas.setColor(pos,Color.RED)
                break

canvas.refresh()
print "done"

