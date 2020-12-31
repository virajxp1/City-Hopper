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

x = ['American Airlines flight departing at 5:50pm from $1,020\nNo change fees\n5:50pm - 11:05am+1\nAustin (AUS) - London (LHR)\n11h 15m (1 stop)\n1h 7m in Dallas (DFW)\nAmerican Airlines\n• American Airlines 6949 operated by British Airways\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 5:50pm from Austin, Landing at 11:05am in London, Priced at $1,020', 'American Airlines flight departing at 10:28am from $1,020\nNo change fees\n10:28am - 6:20am+1\nAustin (AUS) - London (LHR)\n13h 52m (1 stop)\n3h 43m in Dallas (DFW)\nAmerican Airlines\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 10:28am from Austin, Landing at 6:20am in London, Priced at $1,020', 'American Airlines flight departing at 12:40pm from $1,020\nNo change fees\n12:40pm - 8:40am+1\nAustin (AUS) - London (LHR)\n14h 0m (1 stop)\n3h 36m in Chicago (ORD)\nAmerican Airlines\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 12:40pm from Austin, Landing at 8:40am in London, Priced at $1,020', 'American Airlines flight departing at 12:40pm from $1,020\nNo change fees\n12:40pm - 10:15am+1\nAustin (AUS) - London (LHR)\n15h 35m (1 stop)\n5h 11m in Chicago (ORD)\nAmerican Airlines\n• American Airlines 7005 operated by British Airways\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 12:40pm from Austin, Landing at 10:15am in London, Priced at $1,020', 'American Airlines flight departing at 8:15am from $1,020\nNo change fees\n8:15am - 6:20am+1\nAustin (AUS) - London (LHR)\n16h 5m (1 stop)\n5h 51m in Dallas (DFW)\nAmerican Airlines\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 8:15am from Austin, Landing at 6:20am in London, Priced at $1,020', 'American Airlines flight departing at 12:34pm from $1,020\nNo change fees\n12:34pm - 11:05am+1\nAustin (AUS) - London (LHR)\n16h 31m (1 stop)\n6h 21m in Dallas (DFW)\nAmerican Airlines\n• American Airlines 6949 operated by British Airways\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 12:34pm from Austin, Landing at 11:05am in London, Priced at $1,020', 'American Airlines flight departing at 7:30am from $1,020\nNo change fees\n7:30am - 6:20am+1\nAustin (AUS) - London (LHR)\n16h 50m (1 stop)\n6h 37m in Dallas (DFW)\nAmerican Airlines\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 7:30am from Austin, Landing at 6:20am in London, Priced at $1,020', 'American Airlines flight departing at 6:30am from $1,020\nNo change fees\n6:30am - 6:20am+1\nAustin (AUS) - London (LHR)\n17h 50m (1 stop)\n7h 40m in Dallas (DFW)\nAmerican Airlines\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 6:30am from Austin, Landing at 6:20am in London, Priced at $1,020', 'American Airlines flight departing at 10:28am from $1,020\nNo change fees\n10:28am - 11:05am+1\nAustin (AUS) - London (LHR)\n18h 37m (1 stop)\n8h 28m in Dallas (DFW)\nAmerican Airlines\n• American Airlines 6949 operated by British Airways\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for American Airlines flight, departing at 10:28am from Austin, Landing at 11:05am in London, Priced at $1,020', 'Virgin Atlantic flight departing at 5:59pm from $1,020\nNo change fees\n5:59pm - 11:05am+1\nAustin (AUS) - London (LHR)\n11h 6m (1 stop)\n1h 21m in Atlanta (ATL)\nVirgin Atlantic\n• Virgin Atlantic 5018 operated by Delta\n5 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for Virgin Atlantic flight, departing at 5:59pm from Austin, Landing at 11:05am in London, Priced at $1,020', 'Virgin Atlantic flight departing at 3:05pm from $1,020\nNo change fees\n3:05pm - 11:05am+1\nAustin (AUS) - London (LHR)\n14h 0m (1 stop)\n4h 15m in Atlanta (ATL)\nVirgin Atlantic\n• Virgin Atlantic 5020 operated by Delta\n3 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for Virgin Atlantic flight, departing at 3:05pm from Austin, Landing at 11:05am in London, Priced at $1,020', 'Delta flight departing at 11:30am from $1,020\nNo change fees\n11:30am - 7:35am+1\nAustin (AUS) - London (LHR)\n14h 5m (2 stops)\n36m in Atlanta (ATL) • 2h 4m in New York (JFK)\nDelta\n5 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for Delta flight, departing at 11:30am from Austin, Landing at 7:35am in London, Priced at $1,020', 'Delta flight departing at 8:00am from $1,020\nNo change fees\n8:00am - 7:35am+1\nAustin (AUS) - London (LHR)\n17h 35m (2 stops)\n1h 10m in Atlanta (ATL) • 5h 8m in New York (JFK)\nDelta\n5 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for Delta flight, departing at 8:00am from Austin, Landing at 7:35am in London, Priced at $1,020', 'Delta flight departing at 6:30am from $1,020\nNo change fees\n6:30am - 7:35am+1\nAustin (AUS) - London (LHR)\n19h 5m (2 stops)\n3h 46m in Minneapolis (MSP) • 3h 5m in New York (JFK)\nDelta\n5 cleaning and safety practices\n$1,020\nOne way per traveler\nSelect and show fare information for Delta flight, departing at 6:30am from Austin, Landing at 7:35am in London, Priced at $1,020', 'Multiple Airlines flight departing at 5:50pm from $1,028\n5:50pm - 11:05am+1\nAustin (AUS) - London (LHR)\n11h 15m (1 stop)\n1h 7m in Dallas (DFW)\nMultiple airlines\n• Finnair 5492 operated by British Airways\n4 cleaning and safety practices\n$1,028\nOne way per traveler\nSelect and show fare information for multipleAirlines flight, departing at 5:50pm from Austin, Landing at 11:05am in London, Priced at $1,028', 'Multiple Airlines flight departing at 12:34pm from $1,028\nNo change fees\n12:34pm - 6:20am+1\nAustin (AUS) - London (LHR)\n11h 46m (1 stop)\n1h 36m in Dallas (DFW)\nMultiple airlines\n• Finnair 5780 operated by American Airlines\n3 cleaning and safety practices\n$1,028\nOne way per traveler\nSelect and show fare information for multipleAirlines flight, departing at 12:34pm from Austin, Landing at 6:20am in London, Priced at $1,028', '', 'Multiple Airlines flight departing at 12:40pm from $1,028\nNo change fees\n12:40pm - 10:15am+1\nAustin (AUS) - London (LHR)\n15h 35m (1 stop)\n5h 11m in Chicago (ORD)\nMultiple airlines\n• Finnair 5536 operated by British Airways\n3 cleaning and safety practices\n$1,028\nOne way per traveler\nSelect and show fare information for multipleAirlines flight, departing at 12:40pm from Austin, Landing at 10:15am in London, Priced at $1,028', 'Multiple Airlines flight departing at 12:34pm from $1,028\n12:34pm - 11:05am+1\nAustin (AUS) - London (LHR)\n16h 31m (1 stop)\n6h 21m in Dallas (DFW)\nMultiple airlines\n• Finnair 5492 operated by British Airways\n4 cleaning and safety practices\n$1,028\nOne way per traveler\nSelect and show fare information for multipleAirlines flight, departing at 12:34pm from Austin, Landing at 11:05am in London, Priced at $1,028', 'Multiple Airlines flight departing at 7:30am from $1,028\nNo change fees\n7:30am - 6:20am+1\nAustin (AUS) - London (LHR)\n16h 50m (1 stop)\n6h 37m in Dallas (DFW)\nMultiple airlines\n• Finnair 5780 operated by American Airlines\n3 cleaning and safety practices\n$1,028\nOne way per traveler\nSelect and show fare information for multipleAirlines flight, departing at 7:30am from Austin, Landing at 6:20am in London, Priced at $1,028']
#print(parser_expedia(x))