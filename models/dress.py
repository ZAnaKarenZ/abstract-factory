from abc import ABC, abstractmethod

#Abstract class
class Dress(ABC):
    @abstractmethod
    def printDress(self):
        pass
