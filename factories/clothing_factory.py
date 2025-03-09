from abc import ABC, abstractmethod

#Abstract interface
class ClothingFactory(ABC):
    @abstractmethod
    def createOutfit(self):
        pass
    @abstractmethod
    def createDress(self):
        pass