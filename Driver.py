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

    priceMaster = createPriceMaster(Cities,startDate,lengthOfStays)
    price_weights = price_component(priceMaster) #prices have been averaged out
    print(price_weights)

tempMain()