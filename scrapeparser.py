import csv

class Flight(object):
    def __init__(self,airlines,arrival_time,departure_time,origin,destination,price,layovers,duration,days):
        self.airlines = airlines
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination
        self.price = price
        self.layovers = layovers
        self.duration = duration
        self.days = days
    def print(self):
        print("Airlines: " + self.airlines + " From: " +self.origin + "To:" + self.destination + "")
        print("Departs at:" + self.departure_time + " Arrives at:" + self.arrival_time + "")
        print("Layover: " + self.layovers)
        print("Price: $"+ self.price)

# str is a massive string representing webscraped flight data The method outputs a list of objects 'flights' which
# contain arrival/departure location/time and price details for each flight

def parser_expedia(flights):
    data = []
    for flight in flights:
        if not (flight == None or len(flight) == 0):
            row = flight.split("\n")
            if row[1] != "No change fees":
                continue
            times = row[2].split('-')
            days = 0
            if (times[1][-2:] == "+1"):
                times[1] = times[1][:len(times[1]) - 2]
                days = 1
            if (times[1][-2:] == "+2"):
                times[1] = times[1][:len(times[1]) - 2]
                days = 2
            arrival, departure = times[0], times[1]
            locations = row[3].split('-')
            origin, destination = locations[0], locations[1]
            price = row[-3][1:]
            newflight = Flight(row[-5], departure, arrival, origin, destination, price, row[5],row[4],days)
            data.append(newflight)
    return data

