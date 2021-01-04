# This file is for the driver code aka the main will go here
from Scrapper import *
from calculateCost import *
from Graph import solve
from Distancefinder import createDistanceMaster

def Main():
    # simulation data delete later
    Cities = ["New York"]
    startDate = "1/23/2021"
    lengthOfStays = [1]
    Origin = "Austin"
    Cities.insert(0, Origin)

    # put user input here

    priceMaster = createPriceMaster(Cities, startDate, lengthOfStays)
    price_weights = price_component(priceMaster)  # prices have been averaged out
    # print(price_weights)

    # calculate distances
    distanceMaster = createDistanceMaster(Cities)

    # call calculateCost.py . distance_component
    distance_weights = distance_component(distanceMaster)

    # call calculateCost.py . createGraph
    Graph = create_graph(price_weights, distance_weights)

    # get the encoded solution by calling Graph.py.

    optimalPath = solve(Graph)
    optimalFlights = []
    d = 0
    # extract flight data
    # assume top of each matrix is cheapest
    for i in range(len(optimalPath) - 1):
        start = optimalPath[i]
        dest = optimalPath[i + 1]
        flights = priceMaster[start][dest]  # matrix of all flights
        flights = flights[d, :]
        flights = flights[:15]
        flights = flights[flights is not None]
        d += lengthOfStays[dest - 1]
        leavingOrigin = False
        if start == 0:
            leavingOrigin = True
        minFlight = getMinFlight(flights,leavingOrigin)
        optimalFlights.append(minFlight)

    # print out everything

    optimalPath_decoded = []

    for i in range(len(optimalPath)):
        x = Cities[optimalPath[i]]
        optimalPath_decoded.append(x)

    i = 0
    totalCost = 0
    for flight in optimalFlights:
        price = flight.price
        price = int(price.replace(',', ''))
        totalCost += price

    print("Optimal Path is: ")
    path_str = ""
    for i in range(len(optimalPath_decoded)):
        if not (i == len(optimalPath_decoded) - 1):
            path_str += (optimalPath_decoded[i] + " -> ")
        else:
            path_str += (optimalPath_decoded[i])
    print(path_str)
    print("Total cost is: $" + str(totalCost))

    print("Flight details:")

    for flight in optimalFlights:
        flight.print()

Main()
