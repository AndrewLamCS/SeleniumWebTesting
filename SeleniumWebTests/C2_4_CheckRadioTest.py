"""
This script demonstrates how to use Selenium WebDriver to interact with various form elements on a webpage.
It retrieves the path to the ChromeDriver from an environment variable, opens the browser, and performs actions 
such as interacting with checkboxes, radio buttons, and verifying the visibility of elements.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the path from the environment variable.
3. Open a webpage containing various form elements.
4. Interact with checkboxes, radio buttons, and visibility toggles.
5. Validate that the actions (checkbox selection, radio button selection, element visibility) were successful.
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

# Open the specified URL in the browser (the automation practice page)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Locate all checkboxes on the page by their XPath
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Print the total number of checkboxes found on the page
print(len(checkboxes))

# Loop through all checkboxes and select the one with value "option2"
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()  # Click on the checkbox with value "option2"
        assert checkbox.is_selected()  # Assert that the checkbox is selected
        break  # Exit the loop after selecting the checkbox

# Locate all radio buttons by their CSS class
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

# Click the third radio button in the list and assert that it is selected
radiobuttons[2].click()
assert radiobuttons[2].is_selected()  # Assert that the third radio button is selected

# Verify that the text element with the ID "displayed-text" is visible
assert driver.find_element(By.ID, "displayed-text").is_displayed()

# Click the "hide-textbox" button to hide the "displayed-text" element
driver.find_element(By.ID, "hide-textbox").click()

# Assert that the "displayed-text" element is no longer visible
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

# Wait for 2 seconds before closing the browser (just to see the final result)
time.sleep(2)
