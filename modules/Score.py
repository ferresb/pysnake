class Score:
    def __init__(self, interface, cursor, value=0, step=10):
        self.__value        = value
        self.__interface    = interface
        self.__step         = step
        self.__cursor       = cursor

    def increment(self, value = None):
        if (value is None):
            self.__value += self.__step
        else:
            self.__value += value

    def getValue(self):
        return self.__value

    #TODO : write score without moving cursor
    def display(self):
        (maxX, maxY) = self.__interface.getDim()
        self.__interface.writeAt("Score: {}".format(self.__value), maxX+5, 1, self.__cursor.getCoordinates()) 

