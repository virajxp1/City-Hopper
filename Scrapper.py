import numpy as np
import datetime
from Pricechecker import *
from scrapeparser import Flight


def createPriceMaster(Cities, startDate, lengthOfStays):
    # Cities = list of all the cities we have to go through
    master = np.ndarray((len(Cities), len(Cities), sum(lengthOfStays)+1, 25), dtype=np.ndarray)
    # our 4d array which stores top 25 flights^^^

    startDate = datetime.datetime.strptime(startDate, '%m/%d/%Y')
    # get next d days

    dateConverter(startDate)

    Dates = []
    for d in range(0, sum(lengthOfStays) + 1):
        Dates.append(startDate + datetime.timedelta(days=d))

    # create a loop to go through the combinations

    length = len(Cities)

    for i in range(0, length):
        for j in range(0, length):
            if (Cities[i] != Cities[j]):
                m = np.ndarray((sum(lengthOfStays) + 1, 25), dtype=Flight)
                # print(Cities[i], Cities[j])
                for d in range(len(Dates)):
                    # for each date create a matrix
                    convertedDate = dateConverter(Dates[d])
                    currentFlights = getFlights(Cities[i], Cities[j], convertedDate)
                    currentFlights = currentFlights[:25]
                    if (len(currentFlights) != 25):
                        currentFlights.extend([None] * (25 - len(currentFlights)))
                    for x in range(0, 25):
                        m[d][x] = currentFlights[x]
                    # m[d][0].print()
                master[i][j] = m
    # Add a sort by price somewhere in the lower tier classes
    return master


def dateConverter(date):
    # input is a datetime object
    Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    Days = np.arange(1, 31)
    convertedDate = Months[date.month + 1] + " " + str(date.day) + ", " + str(date.year)
    return convertedDate


def getMinFlight(data):
    min = np.inf
    minFlight = None
    for flight in data[0]:
        price = flight.price
        price = int(price.replace(',', ''))
        if (price < min):
            min = price
            minFlight = flight
    return minFlight
