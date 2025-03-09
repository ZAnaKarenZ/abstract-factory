from abc import ABC, abstractmethod
from methods.print_ascii_art import print_ascii_art

#Abstract interface
class ClothingFactory(ABC):
    @abstractmethod
    def createOutfit(self):
        pass
    @abstractmethod
    def createDress(self):
        pass

#Concrete classes
class CasualClothingFactory(ClothingFactory):
    def createOutfit(self):
        return CasualOutfit()
    def createDress(self):
        return CasualDress()
    def qualityReview(self):
        print("Quality review")
        
class ElegantClothingFactory(ClothingFactory):
    def createOutfit(self):
        return ElegantOutfit()
    def createDress(self):
        return ElegantDress()
    def designersMeeting(self):
        print("Desigtners Meeting")

#Abstract classes
class Outfit(ABC):
    @abstractmethod
    def printOutfit(self):
        pass

class Dress(ABC):
    @abstractmethod
    def printDress(self):
        pass

#Concrete classes
class CasualOutfit(Outfit):
    def printOutfit(self):        
        print_ascii_art('CasualOutfit.txt')

class CasualDress(Dress):
    def printDress(self):
        print_ascii_art('CasualDress.txt')

class ElegantOutfit(Outfit):
    def printOutfit(self):
        print_ascii_art('ElegantOutfit.txt')

class ElegantDress(Dress):
    def printDress(self):
        print_ascii_art('ElegantDress.txt')

#Client
class Client:
    def __init__(self, factory, product):
        self.__factory = factory
        self.__product = product

    def deliver(self):
        if self.__product == 'outfit':
            outfit = self.__factory.createOutfit()
            print("Outfit:")
            outfit.printOutfit()

        elif self.__product == 'dress':
            dress = self.__factory.createDress()            
            print("Dress:")
            dress.printDress()


#Main
if __name__ == "__main__":
    #Create factories
    factories = [
        CasualClothingFactory(),
        ElegantClothingFactory()
    ]
    
    type = [
        'outfit',
        'dress'
    ]

    #Deliver to client
    print("Casual Clothing Factory:")
    client = Client(factories[0], type[0])
    client.deliver()
    client = Client(factories[0], type[1])
    client.deliver()
    factories[0].qualityReview()

    print("\nElegant Clothing Factory:")
    client = Client(factories[1], type[0])
    client.deliver()
    client = Client(factories[1], type[1])
    client.deliver()
    factories[1].designersMeeting()