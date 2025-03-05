"""
This script automates a series of actions using Selenium WebDriver with Chrome browser, including:

1. Navigating to the specified URL.
2. Interacting with elements such as buttons, links, and input fields.
3. Adding a specific product (Blackberry) to the cart.
4. Proceeding to checkout and filling out the form to complete the purchase.
5. Verifying the success message upon successful form submission.

The path to the ChromeDriver is fetched from the environment variable 'CHROMEDRIVER_PATH', which allows flexibility in specifying the path based on the user's system configuration.

Usage:
- This script is useful for automating shopping cart interactions, form submissions, and verifying success messages in a web application.
"""

# Import necessary modules from Selenium and os
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get the path to the ChromeDriver from environment variables
chromedriver_path = os.getenv('CHROMEDRIVER_PATH')  # Retrieve the ChromeDriver path from the environment variable

# Initialize the Chrome driver with the specified service
service_obj = Service(chromedriver_path)  # Create a Service object with the ChromeDriver path
driver = webdriver.Chrome(service=service_obj)  # Initialize the Chrome WebDriver with the service object

# Global max wait time for all elements
driver.implicitly_wait(15)  # Set an implicit wait time of 15 seconds for all elements

# Open the specified URL in the browser
driver.get("https://rahulshettyacademy.com/angularpractice/")  # Open the webpage

# Find the element using CSS selector and click on the "Shop" link
driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()  # Click on the 'shop' link

# Collect all the product cards on the page
cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")  # Find all product cards on the page

# Iterate through the cards to find the one with the name "Blackberry"
for card in cards:
    # Get the name of the product on the card
    card_name = card.find_element(By.XPATH, "div/h4/a").text  # Get the product name text
    print(card_name)  # Print the card name to the console

    if card_name == "Blackberry":  # Check if the card is the one with name "Blackberry"
        # Click the "Add to Cart" button on the Blackberry card
        card.find_element(By.XPATH, "div/button").click()  # Click the button to add Blackberry to cart
        break  # Exit the loop once the Blackberry is added to the cart

# Click on the "Checkout" button to proceed to checkout
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()  # Click the 'Checkout' button

# Click on the "Checkout" button again on the next page
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()  # Click the final 'Checkout' button

# Enter "Ind" in the country input field for the country search
driver.find_element(By.ID, "country").send_keys("Ind")  # Type 'Ind' in the country search field

# Wait until the element with link text "India" is present in the dropdown
wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))  # Wait for the 'India' link to appear

# Click on the element with link text "India" from the suggestions
driver.find_element(By.LINK_TEXT, "India").click()  # Click on the 'India' link

# Click on the checkbox to agree with terms and conditions
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()  # Click the checkbox

# Click on the submit button to complete the purchase process
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()  # Click the submit button

# Capture the success message displayed after submission
success_message = driver.find_element(By.CLASS_NAME, "alert-success").text  # Capture success message text
print(success_message)  # Print the success message to the console

# Assert that the success message contains the expected text
assert "Success! Thank you!" in success_message  # Validate that the success message contains "Success! Thank you!"

# Close the browser after completion
driver.quit()  # Close the browser and end the session
