"""
This script demonstrates how to use Selenium WebDriver to interact with input fields and handle browser alerts.
It retrieves the path to the ChromeDriver from an environment variable, opens the browser, and performs the following actions:
- Enters text into an input field.
- Clicks a button that triggers an alert.
- Switches to the alert, retrieves its message, and verifies the entered name in the alert's text.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the path from the environment variable.
3. Open the "Automation Practice" page.
4. Enter a name in an input field, click a button, and handle the alert.
5. Validate the alert message and accept the alert.
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

# Define the name that will be entered in the input field
name = "TESTNAME"

# Open the specified URL in the browser (the automation practice page)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Locate the input field with ID "name" and enter the value defined in the 'name' variable
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)

# Locate the button with ID "alertbtn" and click it to trigger the alert
driver.find_element(By.ID, "alertbtn").click()

# Switch to the alert window
alert = driver.switch_to.alert

# Print the alert message
print(alert.text)

# Assert that the entered name is part of the alert text
assert name in alert.text

# Accept the alert (close it)
alert.accept()  # Use alert.dismiss() if there is a cancel option in the alert

# Wait for 2 seconds before closing the browser (just to see the final result)
time.sleep(2)
