import statistics
import numpy as np


# Takes in array of object flights

def averagecost(flights):
    flights = flights[flights != None]
    if (flights.size ==0 or flights.shape[0] == 0):
        return 0
    prices = []
    for x in flights:
        price = x.price
        price = int(price.replace(',',''))
        prices.append(price)
    low, high = outlier_treatment(prices)
    for x in prices:
        if x > high:
            prices.remove(x)
    average = statistics.mean(prices)
    return average


def outlier_treatment(nums):
    nums.sort()
    #Q1, Q3 = np.percentile(nums, [25, 75])
    Q1, Q3 = np.percentile(nums, [25, 50])
    IQR = Q3 - Q1
    lower_range = Q1 - (2.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    return lower_range, upper_range
