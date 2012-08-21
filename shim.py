class Dim:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "["+str(self.x)+","+str(self.y)+"]"

class Color:
    def __init__(self, red=0, green=0, blue=0, tup=None):
        if tup is not None:
            self.r = tup[0]
            self.g = tup[1]
            self.b = tup[2]
        else:
            self.r = red;
            self.g = green;
            self.b = blue;
    def getTrue(self):
        if -1 not in (self.r, self.g, self.b):
            return int((256*256*float(self.r))+(256*float(self.g))+(self.b))
        else:
            return 1

    def __str__(self):
        return "{r:"+str(self.r)+", g:"+str(self.g)+", b:"+str(self.b)+"}"

Color.black = Color(0,0,0)
Color.white = Color(255,255,255)

class Pixel:
    def __init__(self, pos, color, window):
        self.pos    = pos
        self.color  = color
        self.window = window

    def setColor(self, color=None):
        if color is not None:
            self.window.setPixel(self.pos, color)
        else:
            self.window.setPixel(self.pos, self.color)

    def __str__(self):
        return str(self.pos)+" "+str(self.color)

class Window:
    def __init__(self, fname, title="title", dims=Dim(500,500), color=Color.black):
        self.fname = fname
        self.id   = pmNewImage(0,title, dims.x, dims.y, color.r, color.g, color.b)
        pmOpenImage(self.id, fname)

    def getPixel(self, pos):
        value = pmGetPixelQuickly(self.id, pos.x, pos.y)
        r = value / (256*256)
        g = (value - (r*256*256))/256
        b = (value - (r*256*256) - (g*256))
        return Color(r,g,b)

    def setPixel(self, pos, color):
        # pmSetPixel(self.id, pos.x, pos.y, color.r, color.g, color.b)
        pmSetPixelQuickly(self.id, pos.x, pos.y, color.getTrue())
    def getSize(self):
        return Dim(pmGetImageWidth(self.id), pmGetImageHeight(self.id))

    def refresh(self):
        pmUpdateDisplay(self.id)

    def eachPos(self):
        size = self.getSize()
        for x in range(0, size.x-1):
            for y in range(0, size.y-1):
                yield Dim(x, y)
    def eachColor(self):
        for pos in self.eachPos():
            yield getPixel(pos)
    def eachPixel(self):
        for pos in self.eachPos():
            yield Pixel(pos, self.getPixel(pos), self)

    def pixelsMatching(self, func):
        for pixel in self.eachPixel():
            if func(pixel):
                yield pixel

    def pixelsCompared(self, func):
        bestValue = -2147483646
        best = None
        for pixel in self.eachPixel():
            current = func(pixel)
            if current>best:
                bestValue = current
                best = pixel
        return best;

window = Window(fname = "C:\\Users\\Ty\Pictures\\blur\\fb2.jpg", dims=Dim(500,400))

# Example of lambda select
white = Color(255,255,255)
for pixel in window.eachPixel(): #window.pixelsMatching(lambda p: p.color.r<50 and p.color.g<50 and p.color.b<50):
    pixel.color.r = 255-pixel.color.r
    pixel.color.g = 255-pixel.color.g
    pixel.color.b = 255-pixel.color.b
    pixel.setColor()

window.refresh()

#Set the red component of each Pixel to full
#for pixel in window.eachPixel():
#    pixel.color.r = 255;
#    pixel.set();
#window.refresh();
