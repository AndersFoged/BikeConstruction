class BikeModelEl():
    def __init__(self):
        pass

    @property
    def typeColor(self):
        self.__typeColor = "#FFFFFF" # white
        return self.__typeColor
    
    @typeColor.setter
    def typeColor(self, new_typeColor):
        self.__typeColor = new_typeColor
    