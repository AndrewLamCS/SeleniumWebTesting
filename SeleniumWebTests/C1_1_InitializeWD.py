"""
This script demonstrates how to initialize a WebDriver using different browsers (Chrome, Firefox, Edge),
navigate through webpages, and perform simple actions like back navigation and printing webpage details.
Currently, the Chrome WebDriver is used, but the script also includes the setup for Firefox and Edge (commented out).

Steps:
1. Set up and initialize a WebDriver instance for different browsers.
2. Navigate to specified URLs and perform basic navigation actions.
3. Print webpage details like title and URL.
4. Wait for 5 seconds before closing the browser.
"""
import os
from selenium import webdriver  # Importing WebDriver to interact with the browser
from selenium.webdriver.chrome.service import Service  # Importing Service to set the browser driver executable
import time  # Importing time to add delays in the script

# -- Chrome --
# Specify the path to the ChromeDriver executable
# You can download ChromeDriver from: https://googlechromelabs.github.io/chrome-for-testing/

# Get the path to the ChromeDriver from environment variables
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

# Initialize the Chrome driver with the specified service
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# # -- Firefox --
# Uncomment the code below to use Firefox instead of Chrome
# Specify the path to the Firefox geckodriver executable
# service = Service(executable_path="/Users/alam/Desktop/SeleniumPython/geckodriver")

# # Initialize the Firefox driver with the specified service
# driver = webdriver.Firefox(service=service)

# # -- Edge --
# Uncomment the code below to use Edge instead of Chrome or Firefox
# Specify the path to the Edge driver executable
# service = Service(executable_path="/Users/alam/Desktop/SeleniumPython/edgedriver_arm64/msedgedriver.exe")

# # Initialize the Edge driver with the specified service
# driver = webdriver.Edge(service=service)

# Maximize the browser window for better visibility (optional)
# driver.maximize_window()

# Minimize the browser window (optional)
# driver.minimize_window()

# Open the Google homepage
driver.get("https://rahulshettyacademy.com")

# Print the title of the current webpage to the console
print(f"Title of Webpage: {driver.title}")

# Print the current URL of the webpage to the console
print(f"Present URL: {driver.current_url}")

# Navigate to another URL (Selenium Practice Page)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Navigate back to the previous page (Google homepage)
driver.back()

# Other actions you can perform (currently commented out):
# driver.forward()  # Navigate forward to the next page
# driver.refresh()  # Refresh the current page

# Wait for 5 seconds to allow the page to load and the user to observe the browser
time.sleep(5)

# Close the browser and quit the WebDriver session
driver.quit()
