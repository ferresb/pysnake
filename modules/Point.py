class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.prev = None

    def getXY(self):
        return (self.x, self.y)

    def isEqual(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False

    def belongs(self, points):
        for point in points:
            if self.isEqual(point):
                return True
        return False

    def draw(self, interface, cursor, char='*'):
        interface.drawPoint(self, cursor, char)

    def erase(self, interface, cursor):
        self.draw(interface, cursor, ' ')
        
