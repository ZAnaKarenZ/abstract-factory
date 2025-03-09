""""
Ana Karen Zetter A01637124
Abstract factory model
"""
#Note to self: Unlike C++, there is no need to use #Pragma once (or equivalent) in Python to avoid multiple instances of the same.
from client.client import Client
from factories.casual_clothing_factory import CasualClothingFactory
from factories.elegant_clothing_factory import ElegantClothingFactory

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