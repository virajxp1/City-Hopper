# This file is for the driver code aka the main will go here
from Scrapper import createPriceMaster
from calculateCost import *
from Graph import solve

def Main():
    # simulation data delete later
    Cities = ["New York","Paris"]
    startDate = "1/23/2021"
    lengthOfStays = [1,1]
    Origin = "Austin"
    Cities.insert(0,Origin)

    # put userinput here

    priceMaster = createPriceMaster(Cities,startDate,lengthOfStays)
    price_weights = price_component(priceMaster) # prices have been averaged out
    print(price_weights)

    # calculate distances

    # call calculateCost.py . distance_component

    # call calculateCost.py . createGraph

    Graph = create_graph(price_weights,None)

    # get the encoded solution by calling Graph.py.

    optimalPath = solve(Graph)
    optimalFlights = []
    d = 0
    # extract flight data
    # assume top of each matrix is cheapest
    for i in range(len(optimalPath)-1):
        start = optimalPath[i]
        dest = optimalPath[i+1]
        flights = priceMaster[start][dest] # matrix of all flights
        flights = flights[:,d]
        d+=lengthOfStays[dest-1]
        optimalFlights.append(flights[0])

    # print out everything

    optimalPath_decoded = []

    for i in range(len(optimalPath)):
        if optimalPath[i] == 0:
            optimalPath_decoded.append(Origin)
        else:
            optimalPath_decoded.append(Cities[optimalPath[i]-1])

    i = 0
    totalCost = 0
    for flight in optimalFlights:
        price = flight.price
        price = int(price.replace(',', ''))
        totalCost += price

    print("Optimal Path is: ")
    for i in range(len(optimalPath_decoded)):
        if not (i == len(optimalPath_decoded)-1):
            print(optimalPath_decoded[i] + " -> ")
        else:
            print(optimalPath_decoded[i])
    print("\n")
    print("Total cost is: $" + str(totalCost))

    print("\n")
    print("Flight details:\n")

    for flight in optimalFlights:
        flight.print()

Main()