"""
This script demonstrates how to use Selenium WebDriver to interact with a dropdown search feature on a webpage.
It retrieves the path to the ChromeDriver from an environment variable, opens the browser, and performs the following actions:
- Types a search term in the autosuggest input field.
- Waits for the autosuggest suggestions to appear.
- Selects the country "India" from the suggestions and asserts the input value after selection.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the path from the environment variable.
3. Open the "Dropdowns Practice" page.
4. Interact with the autosuggest search input field.
5. Select a country from the autosuggest list and validate the selection.
"""

import os  # Import os to access environment variables
from selenium import webdriver  # Import WebDriver to interact with the browser
from selenium.webdriver.chrome.service import Service  # Import Service to set up the WebDriver with ChromeDriver
from selenium.webdriver.common.by import By  # Import By to locate elements on the webpage
import time  # Import time for adding delays in the script

# Get the path to the ChromeDriver from environment variables
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

# Initialize the Chrome driver with the specified service (using the ChromeDriver path from the environment variable)
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# Open the specified URL in the browser (the dropdown practice page)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# Locate the autosuggest input field by its ID and type "ind" to trigger the suggestions
driver.find_element(By.ID, "autosuggest").send_keys("ind")

# Wait for 2 seconds to allow the autosuggest suggestions to load
time.sleep(2)

# Locate all the country suggestion elements by their CSS class and store them in the 'countries' list
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

# Print the total number of suggestions available
print(len(countries))

# Loop through the list of country suggestions and click on "India" when it is found
for country in countries:
    if country.text == "India":
        country.click()  # Click the country "India"
        break

# Assert that the selected country (India) is correctly reflected in the input field
# This confirms that the selection process worked as expected
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

# XPATH - Example: //tagname[@attribute='value'] -> //input[@value='Submit']
# CSS - Example: tagname[attribute='value'] -> input[value='Submit']
