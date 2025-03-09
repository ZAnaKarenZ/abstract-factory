from abc import ABC, abstractmethod

#Abstract class
class Outfit(ABC):
    @abstractmethod
    def printOutfit(self):
        pass