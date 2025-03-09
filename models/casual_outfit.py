from models.outfit import Outfit
from methods.print_ascii_art import print_ascii_art

#Concrete class
class CasualOutfit(Outfit):
    def printOutfit(self):        
        print_ascii_art('CasualOutfit.txt')

