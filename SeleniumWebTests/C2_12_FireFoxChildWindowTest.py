"""
This script demonstrates how to switch between parent and child windows using Selenium WebDriver.
It uses Firefox as the browser and interacts with the "The Internet" website to open a new window,
switch to it, print some text from the child window, and then return to the parent window.
Finally, it closes the browser after a short delay.
"""

# Import necessary modules from the Selenium WebDriver library
import os
from selenium import webdriver  # Import WebDriver to interact with the browser
from selenium.webdriver.chrome.service import Service  # Import Service for setting up the browser service
from selenium.webdriver.common.by import By  # Import By to locate elements using various strategies (ID, CSS, etc.)
import time  # Import time module for adding delays
from selenium.webdriver.common.action_chains import ActionChains  # Import ActionChains to perform complex actions

# Set the path for geckodriver (Firefox's WebDriver) using the environment variable
geckodriver_path = os.getenv('GECKODRIVER_PATH')  # Get geckodriver path from environment variables

# Initialize a new instance of the Firefox WebDriver with the specified geckodriver service
service = Service(executable_path=geckodriver_path)  # Pass the geckodriver path to the Service object
driver = webdriver.Firefox(service=service)  # Initialize the Firefox WebDriver with the given service

# Implicit wait to allow the browser to load elements before interacting with them
driver.implicitly_wait(5)  # Set implicit wait time for elements to load

# Open the URL of the test page
driver.get("https://the-internet.herokuapp.com/windows")  # Navigate to the test page

# Find the link with the text "Click Here" and click it to open a new window/tab
driver.find_element(By.LINK_TEXT, "Click Here").click()  # Click on the link to open a new window

# Get a list of all open window handles (this will include both parent and child windows)
windowsOpenList = driver.window_handles  # Get window handles for all open windows

# Switch to the child window (Index 1) to interact with it
driver.switch_to.window(windowsOpenList[1])  # Switch to the second window (child window)

# Print the text inside the <h3> tag of the child window
print(driver.find_element(By.TAG_NAME, "h3").text)  # Print the text inside <h3> tag of the child window

# Close the child window/tab
driver.close()  # Close the currently active (child) window

# Switch back to the parent window (Index 0) after closing the child window
driver.switch_to.window(windowsOpenList[0])  # Switch back to the first window (parent window)

# Assert that the text in the parent window's <h3> tag matches the expected value
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text  # Assert the text in parent window

# Add a 10-second sleep to keep the browser open and visible for observation
time.sleep(10)  # Wait for 10 seconds to keep the browser open

# Quit the browser and close all windows
driver.quit()  # Close the browser and end the WebDriver session
