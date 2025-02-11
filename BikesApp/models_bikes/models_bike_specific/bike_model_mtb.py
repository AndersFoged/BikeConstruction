class BikeModelMtb():
    def __init__(self):
        pass

    @property
    def typeColor(self):
        self.__typeColor = "#005547" # dark green
        return self.__typeColor
    
    @typeColor.setter
    def typeColor(self, new_typeColor):
        self.__typeColor = new_typeColor
    