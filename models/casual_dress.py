from models.dress import Dress
from methods.print_ascii_art import print_ascii_art

#Concrete class
class CasualDress(Dress):
    def printDress(self):
        print_ascii_art('CasualDress.txt')