from abc import ABC, abstractmethod

class BikeAbstract(ABC):
    def __init__(self):
        pass

    #@property
    @abstractmethod
    def typeColor(self):
        pass    
    
    # #@property
    # @abstractmethod
    # def typeColorTest(self):
    #     pass