"""
This script automates interaction with a webpage containing checkboxes and an iframe.
The automation steps include:

1. Navigating to the specified URL.
2. Clicking on checkboxes using Selenium's `ActionChains`.
3. Switching to an iframe and interacting with elements inside it (clicking on a link).
4. The path to the `geckodriver` executable is dynamically fetched from the environment variable.

Before running the script, ensure that the `GECKODRIVER_PATH` environment variable is set to point to the correct location of your `geckodriver` executable.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Fetch the path to the geckodriver from the environment variable 'GECKODRIVER_PATH'
# This makes the script flexible and environment-independent by avoiding hardcoding the geckodriver path.
geckodriver_path = os.getenv('GECKODRIVER_PATH')

# Check if the environment variable is properly set (optional)
if geckodriver_path is None:
    raise ValueError("Please set the 'GECKODRIVER_PATH' environment variable.")

# Initialize the Firefox WebDriver using the geckodriver path obtained from the environment variable
# The Service object is used to specify the geckodriver executable location
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

# Set the global implicit wait time to 5 seconds for element location
driver.implicitly_wait(5)

# Open the specified URL in the browser
# This script will open the "AutomationPractice" page from Rahul Shetty Academy
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Initialize the ActionChains object to perform complex actions like moving to an element and clicking it
action = ActionChains(driver)

# Move to the first checkbox (ID: "checkBoxOption1") and click it
# 'move_to_element' is used to move the mouse to the checkbox element
# 'click' simulates the mouse click
# 'perform()' is called to execute the chained action
action.move_to_element(driver.find_element(By.ID, "checkBoxOption1")).click().perform()

# Move to the second checkbox (ID: "checkBoxOption2") and click it
action.move_to_element(driver.find_element(By.ID, "checkBoxOption2")).click().perform()

# Move to the third checkbox (ID: "checkBoxOption3") and click it
action.move_to_element(driver.find_element(By.ID, "checkBoxOption3")).click().perform()

# Find the iframe element by its ID and switch the driver's focus to the iframe
# This is necessary to interact with elements inside the iframe
iframe = driver.find_element(By.ID, "courses-iframe")
driver.switch_to.frame(iframe)

# Find the "All Access Plan" link inside the iframe using its link text and click it
driver.find_element(By.LINK_TEXT, "All Access Plan").click()

# Optionally, you can add a small wait or perform other actions here if necessary
time.sleep(2)  # Wait for a couple of seconds to observe actions before closing the browser

# Close the browser after completing the test (optional)
driver.quit()
