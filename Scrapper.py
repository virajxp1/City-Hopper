import numpy as np
import datetime

def createPriceMaster(Cities,startDate,lengthOfStays):
    # Cities = list of all the cities we have to go through
    master = np.ndarray((len(Cities),len(Cities),sum(lengthOfStays),25))
    # our 4d array which stores top 25 flights^^^

    startDate = datetime.datetime.strptime(startDate, '%m/%d/%Y')
    # get next d days

    Dates = []
    for d in range(0,sum(lengthOfStays)):
        Dates.append(startDate+datetime.timedelta(days=d))


    # create a loop to go through the combinations
    for i in range(Cities-1):
        for j in range(i,Cities):
            m = np.ndarray((sum(lengthOfStays),25))
            for date in Dates:
                #for each date create a matrix
                print(date)

Cities = ["London","Paris"]
startDate = "1/23/2021"
lengthOfStays = [4,3]
Origin = "Austin"
Cities.insert(0,Origin)
Cities.append((Origin))
createPriceMaster(Cities,startDate,lengthOfStays)