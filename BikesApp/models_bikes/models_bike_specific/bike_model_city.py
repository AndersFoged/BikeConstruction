#from ...models import BikeModelBike
#class BikeModelCity(BikeModelBike):
class BikeModelCity():
    def __init__(self):
        pass

    @property
    def typeColor(self):
        self.__typeColor = "#FF5733" #orange
        return self.__typeColor
    
    @typeColor.setter
    def typeColor(self, new_typeColor):
        self.__typeColor = new_typeColor
    
    def typeColorT(self):
        self.__typeColor = "#FF5733" #orange
        return self.__typeColor