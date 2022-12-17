import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(window_name=new_window)

    x = browser.find_element(By.ID, "input_value")
    num = x.text
    y = calc(num)

    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(y)

    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()

finally:
    time.sleep(30)
    browser.quit()



