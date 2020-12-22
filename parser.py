import csv

#data is a massive string representing webscraped flight data
def parser():
    flights = []
    #Convert txt file to string
    csv_reader = csv.reader("consoleoutput.txt")
    print(csv_reader)

    #Split by ',' and create array of strings

    #Remove ' ' on both sides of string

    #Parse through and append data to 2D array for all info in above 1D array
    
parser()
