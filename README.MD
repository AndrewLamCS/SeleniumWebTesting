# Selenium Python Tests for E-Commerce Website

This repository contains a collection of automated tests written in Python using the Selenium WebDriver. The tests are designed to verify various functionalities of an e-commerce website, ensuring that everything works as expected.

## Files in the Repository:

- **C1_1_InitializeWD.py**: Initializes the WebDriver setup for testing.
- **C2_1_SortWebTablesTest.py**: Tests for sorting functionality in web tables.
- **C2_2_PasswordRecoveryTest.py**: Verifies the password recovery functionality.
- **C2_3_DropDownTest.py**: Tests for dropdown functionality.
- **C2_4_CheckRadioTest.py**: Verifies the behavior of checkbox and radio button elements.
- **C2_5_AlertTest.py**: Ensures that alert dialogs work correctly.
- **C2_6_ShoppingCartTest.py**: Tests shopping cart functionality.
- **C2_7_PromoCodeTest.py**: Validates the use of promo codes on the site.
- **C2_8_ChromeOptions.py**: Configures Chrome options for specific tests.
- **C2_9_SubmitTest.py**: Verifies the behavior of the submission process.
- **C2_10_JavaScriptTest.py**: Tests JavaScript functionality on the site.
- **C2_11_FireFoxFramesTest.py**: Tests for frames and child windows in Firefox.
- **C2_12_FireFoxChildWindowTest.py**: Tests child window handling in Firefox.
- **C2_13_End2EndTest.py**: End-to-end test for the complete e-commerce checkout process.
- **C2_ActionChains.py**: Contains tests involving action chains such as mouse hover and drag-and-drop.

## Setup Instructions:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. **Install Dependencies**:

   Make sure you have Python 3.x installed. Then, install the required packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

3. **WebDriver Setup**:

   You will need to have the corresponding WebDriver for the browser you are testing (e.g., ChromeDriver, GeckoDriver for Firefox). Make sure it's installed and added to your system's PATH.

4. **Running Tests**:

   To run any test, simply execute the script in your terminal:

   ```bash
   python path/to/test_script.py
   ```

## Contributing:

Feel free to fork this repository and submit pull requests for any improvements or additional tests!

## License:

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.
```