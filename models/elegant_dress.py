from models.dress import Dress
from methods.print_ascii_art import print_ascii_art

#Concrete class
class ElegantDress(Dress):
    def printDress(self):
        print_ascii_art('ElegantDress.txt')
