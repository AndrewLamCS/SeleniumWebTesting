"""
This script automates the process of filling out a form on the website "https://rahulshettyacademy.com/angularpractice/"
using Selenium WebDriver. It performs the following tasks:

1. Opens the page in a browser.
2. Enters an email, password, and checks a checkbox.
3. Clicks the submit button and retrieves the success message.
4. Fills in additional form fields like name and radio button selection.
5. Selects a dropdown value (by visible text).
6. Interacts with text fields (entering text, clearing the field).
7. Waits for 30 seconds to observe the behavior before closing the browser.

The ChromeDriver path is dynamically fetched using an environment variable, making the script more flexible for different environments.
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Fetch the path to the ChromeDriver from environment variables
# Use the environment variable CHROMEDRIVER_PATH to dynamically get the path to the ChromeDriver executable
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

# Check if the environment variable is properly set (optional)
if chromedriver_path is None:
    raise ValueError("Please set the 'CHROMEDRIVER_PATH' environment variable.")

# Specify the path to the ChromeDriver executable using the environment variable
# Initialize the ChromeDriver service with the path fetched from the environment variable
service = Service(chromedriver_path)

# Initialize the Chrome driver with the specified service
driver = webdriver.Chrome(service=service)

# Open the specified URL in the browser
# Navigate to the AngularPractice page
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Find the email input field by its name attribute and enter the email
# Use the "name" attribute to locate the email input field and send the email value
driver.find_element(By.NAME, "email").send_keys("test@gmail.com")

# Find the password input field by its ID attribute and enter the password
# Locate the password input field by its "ID" and input a sample password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abc123")

# Find the checkbox by its ID attribute and click it
# Locate the checkbox by its "ID" and check it
driver.find_element(By.ID, "exampleCheck1").click()

# Find the submit button using XPath and click it
# XPath is used to locate elements based on attribute values (in this case, value="Submit")
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# Capture the success message displayed after form submission
# Locate the element containing the success message and print it
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# Find the "name" input field using CSS Selector and enter a name
# CSS Selector is used to locate the name input field by its "name" attribute
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("TestName")

# Click the radio button (by ID) using CSS Selector
# Locate the radio button using its ID and click it
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Static Dropdown - Select by index, visible text, or value
# Locate the dropdown using its ID and create a Select object
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

# Select the option 'Female' by visible text
dropdown.select_by_visible_text('Female')

# Optional: Uncomment the next line to select by index or value
# dropdown.select_by_index(1) # Female
# dropdown.select_by_value('XXXXXX')

# Assert that the success message contains the word "Success"
# Check that the success message is as expected
assert "Success" in message

# Interact with the third text field (clear it and enter new text)
# Find the text field using XPath and enter "HELLOOOO"
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("HELLOOOO")

# Clear the text field and re-enter text
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

# Find the submit button again and click it (to submit the form)
driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# Wait for 30 seconds to keep the browser open and observe the behavior
time.sleep(30)

# Close the browser session
# Close the browser after the test is completed
driver.quit()
