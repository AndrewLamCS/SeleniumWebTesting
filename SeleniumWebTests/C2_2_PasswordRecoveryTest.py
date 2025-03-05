"""
This script demonstrates how to use Selenium WebDriver to interact with a webpage for password recovery functionality.
It retrieves the path to the ChromeDriver from an environment variable, opens the browser, and performs a series of actions 
on a webpage, including navigating to the password recovery section and submitting the required fields.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the path from the environment variable.
3. Open the "Client" page of the website.
4. Interact with the "Forgot password?" link and the form fields to reset the password.
5. Submit the form with the new password.
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

# Open the specified URL in the browser (the client login page)
driver.get("https://rahulshettyacademy.com/client")

# Click on the "Forgot password?" link to navigate to the password recovery section
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# Find the input field for the email address and enter the demo email for password recovery
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

# Find the input field for the new password and enter the new password
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")

# Find the input field for confirming the new password and enter the same password
driver.find_element(By.ID, "confirmPassword").send_keys("Hello@1234")

# Click the "Save New Password" button to submit the form (currently active)
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
