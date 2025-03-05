"""
This script demonstrates how to use Selenium WebDriver for automating a shopping cart process on an e-commerce website.
It retrieves the ChromeDriver path from an environment variable and performs the following tasks:
1. Searches for items on the website and adds them to the cart.
2. Validates the list of products added to the cart.
3. Proceeds to checkout and validates the total amount and sum of the prices.
4. Applies a promo code and validates the discounted price.

Steps:
1. Retrieve the ChromeDriver path from environment variables.
2. Initialize the Chrome WebDriver using the path from the environment variable.
3. Open the shopping page and search for items.
4. Add selected items to the cart and validate the item list.
5. Validate the sum of prices in the cart and compare it to the total amount.
6. Apply a promo code and validate the discount applied.
"""

import os  # Import os to access environment variables
from selenium import webdriver  # Import WebDriver to interact with the browser
from selenium.webdriver.chrome.service import Service  # Import Service to set up the WebDriver with ChromeDriver
from selenium.webdriver.common.by import By  # Import By to locate elements on the webpage
from selenium.webdriver.support.wait import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions  # Import expected_conditions to wait for specific conditions
import time  # Import time for adding delays in the script

# Define the expected product list
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

# Get the path to the ChromeDriver from environment variables
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

# Initialize the Chrome driver with the specified service (using the ChromeDriver path from the environment variable)
service_obj = Service(chromedriver_path)
driver = webdriver.Chrome(service=service_obj)

# Set a global max wait time of 5 seconds for all elements
driver.implicitly_wait(5)

# Open the specified URL in the browser (the shopping page)
driver.get("https://rahulshettyacademy.com/seleniumPractise#/")

# Locate the search input field and type "ber" to search for products
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# Wait for 2 seconds to let the products load (explicit wait would be better here for more control)
time.sleep(2)

# Find all product elements on the page
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# Assert that at least one product is found
count = len(results)
assert count > 0

# Loop through the results and add product names to the actualList
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    # Click on the "Add to Cart" button for each product
    result.find_element(By.XPATH, "div/button").click()

# Assert that the actualList of products matches the expected list
assert expectedList == actualList

# Click on the cart icon to go to the checkout page
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()

# Click on the "PROCEED TO CHECKOUT" button
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation: Retrieve all prices in the cart and calculate the total sum
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)

# Print the calculated sum
print(sum)

# Retrieve the total amount displayed on the page
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

# Assert that the calculated sum matches the displayed total amount
assert sum == totalAmount

# Apply a promo code to get a discount
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# Click on the "Apply" button to apply the promo code
driver.find_element(By.CLASS_NAME, "promoBtn").click()

# Wait until the promo information is visible
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

# Print the promo info message (should display the discount applied)
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# Retrieve the discounted amount displayed on the page
discountedAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

# Assert that the total amount is greater than the discounted amount (i.e., discount was applied)
assert totalAmount > discountedAmount
