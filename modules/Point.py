class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

    def getXY(self):
        return (self.x, self.y)