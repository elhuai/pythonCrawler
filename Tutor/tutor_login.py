import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import credentials from secret module
from secret import tutor_un, tutor_pw

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

# Open TutorABC consultant login page
driver.get("https://consultant.tutorabc.com/views/portal/login/index.html")

try:
    # UPDATED SELECTORS: Target the input elements inside their parent divs
    usernameInput = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.username.ipt-box input"))
    )
    print("Found username field")
    
    passwordInput = driver.find_element(By.CSS_SELECTOR, "div.password.ipt-box input")
    print("Found password field")
    
    # Input credentials
    usernameInput.send_keys(tutor_un)
    passwordInput.send_keys(tutor_pw)
    print("Entered credentials")

    # Use correct selector for the login button div
    submitBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.login-btn.btn"))
    )
    print("Found login button")
    submitBtn.click()
    print("Clicked login button")
    
    # Wait for page to change after login
    current_url = driver.current_url
    WebDriverWait(driver, 15).until(
        lambda driver: driver.current_url != current_url
    )
    print("Login successful")

except Exception as e:
    print(f"Login error: {str(e)}")
    driver.save_screenshot("login_error.png")

# Keep the browser open if needed
# input("Press Enter to close the browser...")
