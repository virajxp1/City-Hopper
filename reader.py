import csv

class City(object):
    # constructor with default values
    def __init__ (self, name, latitude, longitude, country):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.country = country

def reader():
    master = []
    with open('worldcities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            entry = City(row[0], float(row[2]), float(row[3]), row[4])
            master.append(entry)
    return master

def main():
    masterlist = reader()
    print(masterlist)
main()