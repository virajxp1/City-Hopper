import csv

class Flight(object):
    def __init__(self,airlines,departure_time,arrival_time,origin,destination,price,layovers):
        self.airlines = airlines
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination
        self.price = price
        self.layovers = layovers
    def print(self):
        print("Airlines:" + self.airlines + " From:" +self.origin + " To:" + self.destination + "\n")
        print("Departs at:" + self.departure_time + "Arrives at:" + self.arrival_time + "\n")
        print("Layover:" + self.layovers)
        print("\nPrice: $"+ self.price)

# str is a massive string representing webscraped flight data
# The method outputs a list of objects 'flights' which contain arrival/departure location/time and price details for each flight

def parser_expedia(flights):
    data = []
    for flight in flights:
        if not (flight == None or len(flight) == 0):
            row = flight.split("\n")
            if row[1] != "No change fees":
                continue
            times = row[2].split('-')
            if (times[1][-2:] == "+1"):
                times[1] = times[1][:len(times[1]) - 2]
            arrival, departure = times[0], times[1]
            locations = row[3].split('-')
            origin, destination = locations[0], locations[1]
            price = row[-3][1:]
            newflight = Flight(row[-5], departure, arrival, origin, destination, price, row[5])
            data.append(newflight)
    data = flightSort(data)
    return data

def flightSort(data):
    newlist = sorted(data, key=lambda x: x.price, reverse=True)
    return newlist