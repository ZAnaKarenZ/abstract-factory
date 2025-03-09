from factories.clothing_factory import ClothingFactory
from models.elegant_dress import ElegantDress
from models.elegant_outfit import ElegantOutfit

#Concrete class
class ElegantClothingFactory(ClothingFactory):
    def createOutfit(self):
        return ElegantOutfit()
    def createDress(self):
        return ElegantDress()
    def designersMeeting(self):
        print("Desigtners Meeting")
