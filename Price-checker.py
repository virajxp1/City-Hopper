from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import pandas as pd
import time
import os

# these are inputs
Origin = "Austin"
Destination = "New York"
Date = "Jan 12, 2021"

dir_path = os.path.dirname(os.path.realpath(__file__)) # gets current directory path
browser = webdriver.Chrome(executable_path=dir_path + "\\chromedriver.exe") # chrome driver is in current directory
expedia = 'https://www.expedia.com/Flights?tpid=1&eapid=0' # base website
browser.get(expedia) # browser navigates to expedia.com

browser.find_element_by_link_text('One-way').click() # we select 1 way flights since we are doing multiple cities
time.sleep(1)

# this section is to input the origin airport into the leaving from text box
browser.find_element_by_css_selector('[aria-label="Leaving from"]').click()
time.sleep(random.random()*3+.5)
leavingFrom_textfield = browser.find_element_by_css_selector('[data-stid="location-field-leg1-origin-dialog-input"]')
leavingFrom_textfield.send_keys(Origin)
time.sleep(random.random()*3+.5)
leavingFrom_textfield.send_keys("\n")

time.sleep(random.random()*3+.5)
# sleeping so program doesnt crash incase request from script takes longer to
# handle than the time it takes for the script to get to its next instruction

# this section is to input the destination airport into the going to text box
browser.find_element_by_css_selector('[aria-label="Going to"]').click()
time.sleep(random.random()*3+.5)
goingTo_textfield = browser.find_element_by_css_selector('[data-stid="location-field-leg1-destination-dialog-input"]')
goingTo_textfield.send_keys(Destination)
time.sleep(random.random()*3+.5)
goingTo_textfield.send_keys("\n")

time.sleep(random.random()*3+.5)
# input the date into the departure date field
browser.find_element_by_css_selector('[data-stid="open-date-picker"]').click()
dateSelectionString = '[aria-label="' + Date + '"]'
browser.find_element_by_css_selector(dateSelectionString).click() # select the date
time.sleep(random.random()*3+.5)
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

descriptionText = []

for i in range(length):
    z = n[i].text
    descriptionText.append(z) # temporary
    # get the hidden text from each list item

print(descriptionText)

# TODO: here is a list of things that need to be done:
# 1. instead of using a list use a pandas dataframe to store all the text
# 2. Parse the text first by using \n as a delimiter
# 3. Create a list of all the revelant data so price, duration, airlines, layovers, stops, times ...
# 4. Create a google flights API key to get google flights data
# 5. Create an additional script for kayak




