from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, "book")
    button.click()

    num = browser.find_element(By.ID, "input_value")
    x = num.text
    y = calc(x)

    input_text = browser.find_element(By.ID, "answer")
    input_text.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(15)
    browser.quit()


