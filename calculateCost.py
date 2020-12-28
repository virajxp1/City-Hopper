# function that calculates the price component

import numpy as np
from averagecost import averagecost


def price_component(priceMaster):
    # take the price master and spit out a 2d array of price_weights
    price_weights = np.ndarray((priceMaster.shape[0], priceMaster.shape[1]), dtype=int)
    for i in range(priceMaster.shape[0]):
        for j in range(priceMaster.shape[1]):
            average = averagecost(priceMaster[i][j])
            price_weights[i][j] = average

    return price_weights


def distance_component():
    # creates the distance graph
    return None


def create_graph(price_weights, distance_weights):
    # creates optimal distance graph
    return price_weights
