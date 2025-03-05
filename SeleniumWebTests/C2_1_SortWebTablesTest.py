"""
This script demonstrates how to use Selenium WebDriver to interact with a webpage that contains a list of items.
It retrieves the path to the ChromeDriver from an environment variable, opens the browser, interacts with the page, 
and performs sorting validation of items in a table.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the path from the environment variable.
3. Open the "Selenium Practise" page with a list of vegetables.
4. Interact with the page, specifically by clicking the column header to sort the vegetable list.
5. Collect the names of vegetables, check if they are sorted properly, and validate the sorting behavior.
6. Wait for a few seconds for page loading and then close the browser.
"""

import os  # Import os to access environment variables
from selenium import webdriver  # Import WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Import Service to set up the WebDriver with ChromeDriver
from selenium.webdriver.common.by import By  # Import By to locate elements on the webpage
import time  # Import time for adding delays in the script

# Get the path to the ChromeDriver from environment variables
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

# Initialize the Chrome driver with the specified service (using the ChromeDriver path from the environment variable)
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# Open the specified URL in the browser (the page contains a list of vegetable offers)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Wait for 5 seconds to allow the page to load
time.sleep(5)

'''Pseudo code:
Click on column header to sort the vegetable list
Collect all item names --> browserSortedVeggieList (Assuming the browser does not sort properly)
Sort the list manually and compare the two lists to check if sorting is working properly
'''

# Click on the column header ("Veg/fruit name") to trigger the sorting functionality
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# Wait for 5 seconds to allow the sorting to take place
time.sleep(5)

# Collect all vegetable names (from the first column) into a list called veggieWebElements
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

# Create an empty list to store the vegetable names as text (browserSortedVeggieList)
browserSortedVeggieList = []

# Loop through the collected web elements and append their text (vegetable names) to the list
for element in veggieWebElements:
    browserSortedVeggieList.append(element.text)

# Make a copy of the original list of vegetable names
# The copy() method creates a shallow copy of the list to preserve the original state before sorting
originalBrowserSortedList = browserSortedVeggieList.copy()

# Sort the browserSortedVeggieList manually (using Python's built-in sort method)
browserSortedVeggieList.sort()

# Compare the sorted list with the original list to check if sorting works correctly
# If both lists are equal, it means the sorting functionality worked as expected; otherwise, the sorting is broken
assert browserSortedVeggieList == originalBrowserSortedList

# If the assertion passes, print a success message
print("The vegetable list is sorted correctly on the webpage.")

# Close the browser after the test is completed
driver.quit()
