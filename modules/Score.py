class Score:
    def __init__(self, interface, value=0, step=10):
        self.__value        = value
        self.__interface    = interface
        self.__step         = step

    def increment(self, value = None):
        if (value != None):
            self.__value += self.__step
        else:
            self.__value += value

    #TODO : write score without moving cursor
    def display(self):
        (maxX, maxY) = self.__interface.getDim()
        self.__interface.addCenter("Score : {}".format(self.__value), maxY-1)

