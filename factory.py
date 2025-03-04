from abc import ABC, abstractmethod


#Function
def print_ascii_art(file):
    f= open(file,'r')
    print(''.join([line for line in f]))


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
        print_ascii_art('../props/CasualOutfit.txt')

class CasualDress(Dress):
    def printDress(self):
        print_ascii_art('../props/CasualDress.txt')

class ElegantOutfit(Outfit):
    def printOutfit(self):
        print_ascii_art('../props/ElegantOutfit.txt')

class ElegantDress(Dress):
    def printDress(self):
        print_ascii_art('../props/ElegantDress.txt')

