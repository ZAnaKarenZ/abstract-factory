from factories.clothing_factory import ClothingFactory
from models.casual_dress import CasualDress
from models.casual_outfit import CasualOutfit

#Concrete class
class CasualClothingFactory(ClothingFactory):
    def createOutfit(self):
        return CasualOutfit()
    def createDress(self):
        return CasualDress()
    def qualityReview(self):
        print("Quality review")
        