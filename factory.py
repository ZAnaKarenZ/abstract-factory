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

#Abstract class
class Biome:
    @abstractmethod
    def getAnimals(self):
        pass
    def ambientSound(self):
        for animal in self.getAnimals():
            animal.makeSound()

#Concrete classes
class TemperateDeciduousForest(Biome):
    def getAnimals(self):
        return [Bird(), Fish()]

class CoralReef(Biome):
    def getAnimals(self):
        return [Fish()]


#Main function
def main():
    #Forest
    print("Forest sounds:")
    forest = TemperateDeciduousForest()
    forest.ambientSound()

    #Coral reef
    print("Coral reef sounds:")
    reef = CoralReef()
    reef.ambientSound()


if __name__ == "__main__":
    main()