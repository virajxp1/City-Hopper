# This file is for user input

def get_cities():
    print("Enter the cities you want to vist:")
    prompt = ("Hit enter again if you are finished\n")

    line = input(prompt)
    cities = []
    while line:
        cities.append(line)
        line = input()

    return cities


def dates(cities):
    # date needs to be in this format
    print("Enter your prefered start date:")
    startDate = input("Month/Day/Year \nexample '01/01/2021' \n\n")
    lengthOfStay = []
    print("\n")
    for city in cities:
        lengthOfStay.append(input(("Days in " + city + ":")))
    return startDate, lengthOfStay


def OriginCity():
    print("Enter your Origin city:\n")
    Origin = input()
    return Origin

def GetUserInput():
    Origin = OriginCity()
    cities = get_cities()
    startDate, lengthOfStay = dates(cities)
    return Origin, cities, startDate, lengthOfStay
