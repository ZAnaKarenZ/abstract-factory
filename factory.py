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


#Abstract classes
class Outfit:
    @abstractmethod
    def printOutfit(self):
        pass

class Dress:
    @abstractmethod
    def printDress(self):
        pass

#Concrete classes
class CasualOutfit(Outfit):
    def printOutfit(self):
        pass

class CasualDress(Dress):
    def printDress(self):
        pass

class ElegantOutfit(Outfit):
    def printOutfit(self):
        pass

class ElegantDress(Dress):
    def printDress(self):
        pass

