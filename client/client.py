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