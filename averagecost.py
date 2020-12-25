import statistics
import numpy as np

#Takes in array of object flights
def averagecost(flights):
    cost_index = 0
    prices = []
    for x in flights:
        prices.append(x.price)
    low,high = outlier_treatment(prices)
    for x in prices:
        if x < low or x > high:
            prices.remove(x)
    average = statistics.mean(prices)
    return average

def outlier_treatment(nums):
    nums.sort()
    Q1,Q3 = np.percentile(nums,[25,75])
    IQR = Q3 - Q1
    lower_range = Q1 - (2.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    return lower_range,upper_range