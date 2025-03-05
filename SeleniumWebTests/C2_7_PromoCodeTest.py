"""
This script demonstrates how to automate the process of searching for products, adding them to the cart,
and applying a promo code on an e-commerce website using Selenium WebDriver.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the path from the environment variable.
3. Open the shopping page and search for items containing the term "ber".
4. Add all the items to the cart.
5. Proceed to the checkout page and apply a promo code to get a discount.

The script uses environment variables to store the ChromeDriver path for better security and portability.
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

# Set a global max wait time of 5 seconds for all elements
driver.implicitly_wait(5)

# Open the specified URL in the browser (shopping page)
driver.get("https://rahulshettyacademy.com/seleniumPractise#/")

# Locate the search input field and type "ber" to search for products
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# Wait for 2 seconds to let the products load (Implicit wait will not work for obtaining a list of elements)
time.sleep(2)

# Find all product elements on the page
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# Assert that at least one product is found
count = len(results)
assert count > 0

# Loop through the results and click the "Add to Cart" button for each product
for result in results:
    result.find_element(By.XPATH, "div/button").click()  # Chaining XPATH to find the button and click it

# Click on the cart icon to go to the checkout page
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

# Click on the "PROCEED TO CHECKOUT" button
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Locate the promo code input field and type the promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# Click on the "Apply" button to apply the promo code
driver.find_element(By.CLASS_NAME, "promoBtn").click()

# Click on the promo info to verify the promo code result
driver.find_element(By.CLASS_NAME, "promoInfo").click()
