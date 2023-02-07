# imports
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

# open page
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# click on button
button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()

# switch to new window
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# find number
number_one = browser.find_element(By.CSS_SELECTOR, "#input_value")
number = int(number_one.text)
def calc(number):
    return str(math.log(abs(12 * math.sin(number))))
x = calc(number)

# find answer field
answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
answer_field.send_keys(x)

# click on submit
submit_button = browser.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

# sleep
time.sleep(5)

# close browser
browser.close()
browser.quit()

# empty line

