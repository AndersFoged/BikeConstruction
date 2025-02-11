class BikeModelRoad():
    def __init__(self):
        pass

    @property
    def typeColor(self):
        self.__typeColor = "#fce300" # yellow
        return self.__typeColor
    
    @typeColor.setter
    def typeColor(self, new_typeColor):
        self.__typeColor = new_typeColor
    