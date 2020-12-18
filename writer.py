import csv

class City(object):
    # constructor with default values
    def __init__ (self, name, latitude, longitude, country):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.country = country

def writer(newcity):
    with open('worldcities.csv', "a+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([newcity.name,newcity.latitude,newcity.longitude,newcity.country])

def main():
    city = City("Kilifi",3.5107,39.9093,"Kenya")
    writer(city)
    newcity = City("Shankar", 4.1239, 39.9093, "Tanzania")
main()