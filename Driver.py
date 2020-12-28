# This file is for the driver code aka the main will go here
from Scrapper import createPriceMaster
from calculateCost import price_component


def tempMain():
    # simulation data
    Cities = ["London","Paris", "Munich"]
    startDate = "1/23/2021"
    lengthOfStays = [1,1,1]
    Origin = "Austin"
    Cities.insert(0,Origin)

    # put userinput here

    priceMaster = createPriceMaster(Cities,startDate,lengthOfStays)
    price_weights = price_component(priceMaster) #prices have been averaged out
    print(price_weights)

    # calculate distances

    # call calculateCost.py . distance_component

    # call calculateCost.py . createGraph

    # get the encoded solution by calling Graph.py.

    # decode the optimal path

    # extract flight data


tempMain()