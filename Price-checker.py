from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapeparser import parser_expedia
import random
import time
import os

## EXPEDIA ##

def ExpediaScraper(Origin,Destination,Date):
    dir_path = os.path.dirname(os.path.realpath(__file__)) # gets current directory path

    browser = webdriver.Chrome(executable_path=dir_path + "\\chromedriver.exe") # chrome driver is in current directory
    expedia = 'https://www.expedia.com/Flights?tpid=1&eapid=0' # base website
    browser.get(expedia) # browser navigates to expedia.com

    browser.find_element_by_link_text('One-way').click()  # we select 1 way flights since we are doing multiple cities

    # this section is to input the origin airport into the leaving from text box
    browser.find_element_by_css_selector('[aria-label="Leaving from"]').click()
    time.sleep(random.random()+.5)
    leavingFrom_textfield = browser.find_element_by_css_selector('[data-stid="location-field-leg1-origin-dialog-input"]')
    leavingFrom_textfield.send_keys(Origin)
    time.sleep(random.random()+.5)
    leavingFrom_textfield.send_keys("\n")

    time.sleep(random.random()+.5)
    # sleeping so program doesnt crash incase request from script takes longer to
    # handle than the time it takes for the script to get to its next instruction

    # this section is to input the destination airport into the going to text box
    browser.find_element_by_css_selector('[aria-label="Going to"]').click()
    time.sleep(random.random()+.5)
    goingTo_textfield = browser.find_element_by_css_selector('[data-stid="location-field-leg1-destination-dialog-input"]')
    goingTo_textfield.send_keys(Destination)
    time.sleep(random.random()+.5)
    goingTo_textfield.send_keys("\n")

    time.sleep(random.random()+.5)
    # input the date into the departure date field
    browser.find_element_by_css_selector('[data-stid="open-date-picker"]').click()
    dateSelectionString = '[aria-label="' + Date + '"]'
    time.sleep(random.random()+.5)
    browser.find_element_by_css_selector(dateSelectionString).click() # select the date
    time.sleep(random.random()+.5)
    browser.find_element_by_css_selector('[data-stid="apply-date-picker"]').click()# select "Done"

    # hit the search button to pull up all the flights
    browser.find_element_by_css_selector('[data-testid="submit-button"]').click()

    time.sleep(10) # give it time to load

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


def KayakScraper(Origin,Destination,Date):
    ## Kayak ##
    dir_path = os.path.dirname(os.path.realpath(__file__)) # gets current directory path
    browser = webdriver.Chrome(executable_path=dir_path + "\\chromedriver.exe") # chrome driver is in current directory
    Kayak = 'https://www.kayak.com/flights'
    browser.get(Kayak) # browser navigates to Kayak
    time.sleep(1)
    # Select one-way
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[1]/div[1]').click()
    time.sleep((.5))
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul/li[2]').click()
    time.sleep(.5)

    # check if there is a preselected city
    try:
        browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]').click()
        browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div[3]/input').send_keys("\n")
    except:
        pass

    # input origin city
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[2]').click()
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[1]/div/div/div').click()
    time.sleep(.1)
    browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div[3]/input').send_keys(Origin+"\n")
    time.sleep(1)

    # input destination city
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[3]').click()
    browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[3]/input').send_keys(Destination+"\n")
    time.sleep(1)

    # input date
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[1]/div/div/div[1]/div/div/section[2]/div/div/div[2]/form[1]/div[1]/div/div[1]/div/div[4]/div/div[1]/div/div').click()

    # For date to enter it u need to use the arrow keys so take the input date take the current date preset and then right arrow or left arrow in a loop untill you get to the right date


