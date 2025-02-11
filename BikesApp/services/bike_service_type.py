from BikesApp.models_bikes.models_bike_specific.bike_model_road import BikeModelRoad
from BikesApp.models_bikes.models_bike_specific.bike_model_mtb import BikeModelMtb
from BikesApp.models_bikes.models_bike_specific.bike_model_gravel import BikeModelGravel
from BikesApp.models_bikes.models_bike_specific.bike_model_city import BikeModelCity
from BikesApp.models_bikes.models_bike_specific.bike_model_downhill import BikeModelDovnhill
from BikesApp.models_bikes.models_bike_specific.bike_model_tandem import BikeModelTandem
from BikesApp.models_bikes.models_bike_specific.bike_model_el import BikeModelEl
#from storages.bike_storage_type import BikeStorageType

class BikeServiceType:
    def __init__(self):
        pass

        
    def get_type_color(self, allBikes) -> list:
        self.__bikeRoad = BikeModelRoad()
        self.__bikeMtb = BikeModelMtb()
        self.__bikeGravel = BikeModelGravel()
        self.__bikeCity = BikeModelCity()
        self.__bikeDownhill = BikeModelDovnhill()
        self.__bikeTandem = BikeModelTandem()
        self.__bikeEl = BikeModelEl()

        for bike in allBikes:
            if bike.typeId:
                match bike.typeId:
                    case 1:  # City
                        bike.typeColor = self.__bikeCity.typeColor
                    case 2:  # Road
                        bike.typeColor = "#fce300"  # yellow
                    case 3:  # MTB
                        bike.typeColor = self.__bikeMtb.typeColor
                    case 4:  # Gravel
                        bike.typeColor = self.__bikeGravel.typeColor
                    case 5:  # Tandem
                        bike.typeColor = self.__bikeTandem.typeColor
                    case 6:  # El
                        bike.typeColor = self.__bikeEl.typeColor
                    case _:
                        continue  # Skip invalid types

                # **Ensure the bike is saved**
                bike.save()
