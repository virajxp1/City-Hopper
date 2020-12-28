import math
from reader import reader
#Finds distance between two cities given two city names
def distancefinder(city1,state1,country1,city2,state2,country2):
    master = reader()
    for x in master:
        if x.name == city1 and x.country == country1 and x.state == state1:
            lat1 = x.latitude
            lon1 = x.longitude
        elif x.name == city2 and x.country == country2:
            lat2 = x.latitude
            lon2 = x.longitude

    #The following is based off of Haversine's formula to determine the great-circle distance between two points
    R = 6371000     # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # output distance in meters
    return d

def createDistanceMaster(Cities):
    return None