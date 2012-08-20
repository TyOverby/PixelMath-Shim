class Dim:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    def __init__(self, red, green, blue, tup=None):
        if tup is not None:
            self.r = tup[0]
            self.g = tup[1]
            self.b = tup[2]
        else:
            self.r = red;
            self.g = green;
            self.b = blue;

Color.black = Color(0,0,0)
Color.white = Color(255,255,255)

class Pixel:
    def __init__(self, pos, color):
        self.pos   = pos
        self.color = color

class Window:
    def __init__(self, fname, title="title", dims=Dim(500,500), color=Color.black):
        self.fname = fname
        self.id   = pmNewImage(0,title, dims.x, dims.y, color.r, color.g, color.b)
        pmOpenImage(self.id, fname)

    def getPixel(pos):
        return pmGetPixel(self.id, pos.x, pos.y)

    def setPixel(pos, color):
        pmSetPixel(self.id, pos.x, pos.y, color.r, color.g, color.b)

    def getSize():
        size = pmGetScreenSize()
        return Dim(size[0],size[1])

    def refresh():
        pmRefresh(self.id)

    def eachPos():
        size = self.getSize()
        for x in range(0, size.x):
            for y in range(0, size.y):
                yield Dim(x, y)
    def eachColor():
        for pos in self.eachPos():
            yield getPixel(pos)
    def eachPixel():
        for pos in self.eachPos():
            yield Pixel(pos, getPixel(pos))



