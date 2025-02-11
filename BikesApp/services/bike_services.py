from ..models import BikeModelBike
# from viewmodels.bike_viewmodel_create_update import BikeViewModuelCreateUpdate
# from storages.bike_storage_bike import BikeStorageBike
#from .bike_service_type import BikeServiceType
 
class BikeServiceBike:
    def __init__(self):
        pass
        #self.__storageBike = BikeStorageBike()
        #self.__bikeServiceType = BikeServiceType()

    # def get_all_bikes(self):
    #     allBikes = self.__storageBike.get_all_bikes()
    #     self.__bikeServiceType.get_type_color(allBikes)
    #     allBikes = self.reverse_list(allBikes)
    #     return allBikes
    
    def reverse_list(self, list) -> list:
        #allBikes.reverse()
        list = list[::-1]
        #print(f'See --> {allBikes}')
        return list
       
    # def get_bike(self, bikeID):
    #     for p in self.get_all_bikes():
    #         if p.bikeID == bikeID:
    #             return p
    #     else:
    #         return None

    # def create_bike(self, bikeViewModuelCreateUpdate:BikeViewModuelCreateUpdate):
    #     return self.__storageBike.create_bike(bikeViewModuelCreateUpdate)  
 
    # def update_bike(self, bike:BikeModelBike):
    #     bike_types = self.__bikeServiceType.get_all_types()
    #     index = bike_types.index(str(bike.typeID))
    #     bike.typeID = index + 1
    #     self.__storageBike.update_bike(bike)
    #     return bike
    
    # def delete_bike(self, bikeID):
    #     self.__storageBike.delete_bike(bikeID)
