"""
This script demonstrates how to use Selenium WebDriver with custom ChromeOptions to control browser behavior,
while using an environment variable to set the path for the ChromeDriver executable.

1. Retrieves the ChromeDriver path from the environment variable 'CHROMEDRIVER_PATH'.
2. Sets up ChromeOptions to:
    - Start the browser maximized.
    - Run the browser in headless mode (without a GUI).
    - Ignore SSL certificate errors.

3. Initializes the Chrome WebDriver with the specified service and options.

4. Opens a website (https://rahulshettyacademy.com/angularpractice/) and prints the page title.

Usage:
- This script is useful for running Selenium tests or automation tasks in headless mode, especially when interacting with web pages that may contain SSL certificate errors or require the browser to run in the background.

# Resource: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

"""

# Resource: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

# Import necessary modules from Selenium and os
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Required for ChromeDriver service setup

# Get the path to the ChromeDriver from environment variables
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')  # Retrieve ChromeDriver path from environment variable

# chromeOptions - use add_argument() to provide necessary arguments for browser behavior
chrome_options = webdriver.ChromeOptions()

# Add an argument to start the browser maximized
chrome_options.add_argument("--start-maximized")  # Start the browser maximized

# Add an argument to run the browser in headless mode (without GUI)
chrome_options.add_argument("--headless")  # Run the browser in headless mode (no GUI)

# Add an argument to ignore SSL certificate errors
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore certificate errors

# Initialize the Chrome WebDriver with the specified executable path and options
service = Service(chromedriver_path)  # Use the environment variable for ChromeDriver path

# Create an instance of Chrome WebDriver with the service and chrome options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the specified URL
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Print the title of the webpage
print(driver.title)

