class LinkedList:
    def __init__(self, point=None):
        self.head = point
        self.tail = point
        self.__length = 1 if point != None else 0

    def addElemLast(self, point):
        self.tail.next = point
        point.prev = self.tail
        self.tail = point
        self.__length += 1

    def remElemLast(self):
        if self.__length > 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.__length -= 1

    def addElemFirst(self, point):
        self.head.prev = point
        point.next = self.head
        self.head = point
        self.__length += 1

    def remElemFirst(self):
        if self.__length > 1:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

    def getPoints(self):
        curr = self.head
        points = []
        while curr != None:
            points.append(curr)
            curr = curr.next
        return points 
