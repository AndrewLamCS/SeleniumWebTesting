"""
This script demonstrates how to automate a browser using Selenium WebDriver in headless mode, 
where the browser window is not visible during execution. It performs the following tasks:

1. Opens the webpage "https://rahulshettyacademy.com/AutomationPractice/" in headless mode.
2. Scrolls down the page multiple times by a specific amount (400 pixels) with small pauses between scrolls for smooth scrolling.
3. Takes a screenshot of the page after scrolling and saves it as "screenshot.png" (useful for debugging purposes, e.g., in case of test failures).

The ChromeDriver path is obtained using an environment variable, which allows for a more flexible configuration of the script.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Fetch the path to the ChromeDriver from environment variables
# Use the environment variable CHROMEDRIVER_PATH to dynamically get the path to the ChromeDriver executable
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

# Headless mode - run without opening a browser window
# Create a ChromeOptions object to customize the browser behavior
chrome_options = webdriver.ChromeOptions()  

# Add the argument to run the browser in headless mode (no GUI)
chrome_options.add_argument("headless")  

# Add the argument to ignore SSL certificate errors
chrome_options.add_argument("--ignore-certificate-errors")  

# Initialize the ChromeDriver with the specified service and options (headless mode)
# Set the path to ChromeDriver using the environment variable
service_obj = Service(chromedriver_path)  

# Launch Chrome in headless mode
driver = webdriver.Chrome(service=service_obj, options=chrome_options)  

# Open the specified URL in the browser
# Navigate to the AutomationPractice webpage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")  

# Scroll down the page multiple times
# Loop to scroll 5 times (adjustable)
for i in range(5):  
    # Scroll the page down by 400 pixels each time
    driver.execute_script("window.scrollBy(0, 400);")  
    
    # Add a small delay of 1 second for smoother scrolling effect
    time.sleep(1)  

# Save a screenshot (after scrolling) - can be used on test failures or for debugging
# Capture a screenshot of the page and save it as 'screenshot.png'
driver.get_screenshot_as_file("screenshot.png")  

# Close the browser session after the operations are complete
# Close the browser and end the WebDriver session
driver.quit()  
