from abc import ABC, abstractmethod

#Abstract interface
class ClothingFactory:
    @abstractmethod
    def createOutfit(self):
        pass
    @abstractmethod
    def createDress(self):
        pass

#Concrete classes
class CasualClothingFactory(ClothingFactory):
    def createOutfit(self):
        pass
    def createDress(self):
        pass

class ElegantClothingFactory(ClothingFactory):
    def createOutfit(self):
        pass
    def createDress(self):
        pass