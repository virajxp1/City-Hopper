from turtle import pd
from selenium import webdriver
from scrapeparser import parser_expedia
import random
import time
import os
from datetime import datetime, timedelta
import smtplib
import calendar

## EXPEDIA ##

def ExpediaScraper(Origin,Destination,Date):
    dir_path = os.path.dirname(os.path.realpath(__file__)) # gets current directory path
    cwd = os.getcwd() + "/chromedriver 2"
    browser = webdriver.Chrome(executable_path=cwd) # chrome driver is in current directory
    #browser.maximize_window()
    expedia = 'https://www.expedia.com/Flights?tpid=1&eapid=0' # base website
    browser.get(expedia) # browser navigates to expedia.com

    browser.find_element_by_link_text('One-way').click()  # we select 1 way flights since we are doing multiple cities

    # this section is to input the origin airport into the leaving from text box
    browser.find_element_by_css_selector('[aria-label="Leaving from"]').click()
    time.sleep(random.random()+.5)
    leavingFrom_textfield = browser.find_element_by_css_selector('[data-stid="location-field-leg1-origin-menu-input"]')
    leavingFrom_textfield.send_keys(Origin + "\n")
    time.sleep(random.random()+.5)
    # sleeping so program doesnt crash incase request from script takes longer to
    # handle than the time it takes for the script to get to its next instruction

    # this section is to input the destination airport into the going to text box
    browser.find_element_by_css_selector('[aria-label="Going to"]').click()
    time.sleep(random.random()+.5)
    goingTo_textfield = browser.find_element_by_css_selector('[data-stid="location-field-leg1-destination-menu-input"]')
    goingTo_textfield.send_keys(Destination+"\n")
    time.sleep(random.random()+.5)
    # input the date into the departure date field
    browser.find_element_by_css_selector('[id="d1-btn"]').click()

    dateSelectionString = '[aria - label = "' + Date + '"]'
    time.sleep(random.random()+.5)
    dateButton = browser.find_element_by_css_selector(dateSelectionString) # select the date
    browser.execute_script("arguments[0].scrollIntoView();", dateButton)
    time.sleep(random.random()+.5)
    dateButton.click()
    time.sleep(random.random()+.5)
    browser.find_element_by_css_selector('[data-stid="apply-date-picker"]').click()# select "Done"

    # hit the search button to pull up all the flights
    browser.find_element_by_css_selector('[data-testid="submit-button"]').click()

    time.sleep(15) # give it time to load

    # pull the ordered list from the html
    ol = browser.find_element_by_id("flightModuleList")
    # create list for each list item in the ordered list
    n = ol.find_elements_by_tag_name("li")
    for i in n:
        if 144 not in i.size.values():
            n.remove(i) # remove ads/extranious cards
    length = len(n)

    descriptionText_expedia = []

    for i in range(length):
        z = n[i].text
        descriptionText_expedia.append(z) # temporary
        # get the hidden text from each list item
    browser.quit()
    return parser_expedia(descriptionText_expedia)

## KAYAK ##
class KayakData(object):
    # constructor with default values
    def __init__(self, date,data,price):
        self.date = date
        self.data = data
        self.price = price
def KayakScraper(origin,destination,startdate,enddate):
    #options = Options()
    #options.add_argument("--disable-notifications")
    ## Kayak ##
    dir_path = os.path.dirname(os.path.realpath(__file__)) # gets current directory path
    cwd = os.getcwd() + "/chromedriver 2"
    browser = webdriver.Chrome(executable_path=cwd)  # chrome driver is in current directory
    Kayak = 'https://www.kayak.com/flights/' + origin + '-' + destination + '/' + str(startdate) + '/' + str(enddate)
    Kayak2 = 'https://www.kayak.com/flights/' + origin + '-' + destination + '/' + str(startdate) + '/' + str(enddate) + "?sort=cheapest"
    browser.get(Kayak) # browser navigates to Kayak
    time.sleep(6)

    #Close pop-up
    Kayakclosepopup(browser)

    scrapablepage = False
    #Change to one-way
    while(scrapablepage == False):
        try:
            browser.find_elements_by_xpath('//*[contains(@id,"switch-display")]')[0].click()
            browser.find_element_by_xpath('//*[contains(@id,"switch-option-2")]').click()
            time.sleep(3)
            browser.find_elements_by_xpath('//*[contains(@id,"-submit")]')[0].click()
            time.sleep(3)
            scrapablepage = True
        except:
            browser.get(Kayak2)
            time.sleep(2)
            Kayakclosepopup(browser)
            '''browser.find_elements_by_xpath('//*[contains(@id,"-location")]')[0].click()
            time.sleep(2)
            browser.find_element_by_xpath('//*[contains(@id,"switch-display-status")]').click()
            browser.find_element_by_xpath('//*[contains(@id,"switch-option-2")]').click()
            time.sleep(1)
            browser.find_elements_by_xpath('//*[contains(@id,"-submit")]')[0].click()
            time.sleep(3)'''

    cheap_results = '//a[@data-code = "price"]'
    try:
        browser.find_element_by_xpath(cheap_results).click()
        time.sleep(3)
    except:
        pass

    #Load more results - each call adds 15 flights to the sample size
    Kayakloadmore(browser)

    #Scrape flight time/layover data from page
    xp_sections = '//*[@class="mainInfo"]'
    sections = browser.find_elements_by_xpath(xp_sections)
    sections_list = [value.text for value in sections]
    print(sections_list)
    print(len(sections_list))


    #Scrape flight price data
    #price2list = browser.find_elements_by_xpath('//*[@class,"col-price result-column js-no-dtog"]')
    prices = browser.find_elements_by_xpath('//*[contains(@class,"col-price result-column")]')
    prices_list = [price.text for price in prices]
    #print(len(price2list))
    print(prices_list)
    print(len(prices_list))
    return sections_list

def Kayakclosepopup(browser):
    closepopup = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close inside darkIcon")]'
    try:
        browser.find_element_by_xpath(closepopup).click()
        time.sleep(6)
    except:
        pass

def Kayakloadmore(browser):
    try:
        browser.find_elements_by_xpath('//*[contains(@id,"-loadMore")]')[0].click()
        time.sleep(3)
    except:
        pass

def dateprocessor(date):
    abbr_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
    split = date.split()
    month = int(abbr_to_num[split[0]])
    year = int(split[2])
    day = int(split[1][0:-1])
    startdate = datetime(year,month,day)
    return startdate.date()

def GoogleFlightsApiScrapper():
    return None


def getFlights(Origin,Destination,Date):
    ExpediaFlights = ExpediaScraper(Origin,Destination,Date)
    return ExpediaFlights

def getKayakflights(origin,destination,date,duration):
    startdate = dateprocessor(date)
    enddate = startdate + timedelta(duration)
    currentdate = startdate
    flightmaster = []
    for x in range(duration):
        flightdata = KayakScraper(origin,destination,currentdate,enddate)
        flight = KayakData(currentdate,flightdata,2)
        flightmaster.append(flight)
        currentdate = startdate + timedelta(1)

    return flightmaster
def test():
    origin = 'AUS'
    destination = 'BOM'
    date = 'Jun 5, 2021'
    print(getKayakflights(origin,destination,date,2))
test()