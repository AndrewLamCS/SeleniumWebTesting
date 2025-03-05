"""
This script demonstrates how to use Selenium WebDriver with Chrome to perform automated browser interactions.
It includes actions like maximizing the browser window, navigating to a URL, performing mouse hover actions, 
and interacting with context menu items using ActionChains.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the specified ChromeDriver path.
3. Implicitly wait for 5 seconds for elements to be available before throwing an exception.
4. Maximize the browser window.
5. Navigate to a URL.
6. Use ActionChains to perform mouse hover actions and click on a specific link.

Note: This code assumes the ChromeDriver path is stored in an environment variable 'CHROMEDRIVER_PATH'.
"""


import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# Get the path to the ChromeDriver from environment variables
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

# Initialize the Chrome driver with the specified service
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# Implicitly wait for 5 seconds for elements to be available before throwing an exception
driver.implicitly_wait(5)

# Maximize the browser window
driver.maximize_window()

# Open the specified URL in the browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Create an object of ActionChains to perform complex user interactions
action = ActionChains(driver)

# Move the mouse to the element with the ID 'mousehover' and perform the action
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()