import numpy as np
import datetime
from Pricechecker import *
from scrapeparser import Flight
from datetime import timedelta


def createPriceMaster(Cities, startDate, lengthOfStays):
    # Cities = list of all the cities we have to go through
    master = np.ndarray((len(Cities), len(Cities), sum(lengthOfStays) + 1, 25), dtype=np.ndarray)
    # our 4d array which stores top 25 flights^^^

    startDate = datetime.datetime.strptime(startDate, '%m/%d/%Y')
    # get next d days

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
    convertedDate = Months[date.month - 1] + " " + str(date.day) + ", " + str(date.year)
    return convertedDate


def getMinFlight(data_input, leavingOrigin):
    data = data_input
    minCost = np.inf
    data = data[0]
    data = list(data)
    minFlight = None
    for flight in data:
        price = flight.price
        price = int(price.replace(',', ''))
        if price < minCost:
            # find cheapest flight value
            minCost = price
            minFlight = flight
    # now look at all flights within 5% of this value

    optimized = []
    for flight in data:
        price = flight.price
        price = int(price.replace(',', ''))
        if price < 1.05 * minCost:
            optimized.append(flight)

    data = optimized
    # find flights with smallest durations
    durations = []
    times = []
    for flight in data:
        a = flight.arrival_time
        a = a.replace(" ", "")
        a_t = a[-2:]
        a = a[:-2]
        a_t = a_t.upper()
        a = a + a_t
        d = flight.departure_time
        d = d.replace(" ", "")
        d_t = d[-2:]
        d = d[:-2]
        d_t = d_t.upper()
        d = d + d_t
        FMT = '%I:%M%p'
        a = datetime.datetime.strptime(a, FMT)
        d = datetime.datetime.strptime(d, FMT)

        times.append(d)
        dur = a - d
        dur = dur / timedelta(minutes=1)
        if flight.days == 1:
            dur = 1440 + dur
        if flight.days == 2:
            dur += (2 * 1440)
        durations.append(dur)

    minDuration = min(durations)

    optimized = []
    times_optimized = []
    i = 0
    for flight in data:
        duration = durations[i]
        if duration < 1.25 * minDuration:
            optimized.append((flight, i))
            times_optimized.append(times[i])
        i += 1

    data = optimized
    try:
        earliest = min(times_optimized)
        latest = max(times_optimized)
        Optimalflight = None
        if leavingOrigin:
            # find the earliest flight to leave
            for flight, index in data:
                if times[index] == earliest:
                    Optimalflight = flight
        else:
            # find the latest flight to leave - maximize time
            for flight, index in data:
                if times[index] == latest:
                    Optimalflight = flight

        if Optimalflight is None:
            Optimalflight = minFlight

        return Optimalflight
    except:
        pass
        return minFlight
