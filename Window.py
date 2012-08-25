class Window:
    def __init__(self, fname=None, title="title", dims=Dim(500,500), color=Color.black):
        self.fname = fname
        self.id   = pmNewImage(0,title, dims.x, dims.y, color.r, color.g, color.b)
        if fname is not None:
            pmOpenImage(self.id, fname)

    def getColor(self, pos):
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
            yield self.getColor(pos)
    def eachPixel(self):
        for pos in self.eachPos():
            yield Pixel(pos, self.getColor(pos), self)

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
    def inBounds(self, position):
        size = self.getSize()
        x = size.x>position.x and 0 < position.x
        y = size.y>position.y and 0 < position.y
        return x and y
