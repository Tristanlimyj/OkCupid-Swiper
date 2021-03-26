from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re, time, random, os
from dotenv import load_dotenv
from common_functions import *

load_dotenv()

driver = webdriver.Firefox()
driver.get("https://www.okcupid.com/home")

# Wait for the page to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'username'))
)
# Check if it is in the Login Page
url = driver.current_url

if re.match('https://www.okcupid.com/login', url):
    # Input the Acc Data
    insert_into_field(driver, 'input#username', os.getenv('OKC_USERNAME'))
    insert_into_field(driver, 'input#password', os.getenv('PASSWORD'))
    # Click Login Btn
    click_btn(driver, "button.login-actions-button")
    # Try to get the 2FA class else pass
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.login-header-title-SMS_TWO_FACTOR'))
        )
        click_btn(driver, "button.login-actions-button")
        # Get the 2FA
        otp_password = input('Input the OTP Password : ')
        # 2FA input field
        two_fa_input = driver.find_elements_by_class_name('code-inputs-digit')
        
        for index in range(len(two_fa_input)):
            two_fa_input[index].send_keys(int(otp_password[index]))

        click_btn(driver, "button.login-actions-button")

    except Exception as e:
        pass
# Wait for the Page to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'stacks-menu'))
)

# To get all the categories
categories = driver.find_elements_by_class_name('stacks-menu-item')

for category in categories:
    category.click()
    while True:
        sleep_time = random.randint(1,2)
        time.sleep(sleep_time)
        try:
            like_btn = driver.find_element_by_css_selector("button.likes-pill-button")
            like_btn.click()
        except:
            break
driver.close()
