import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestInp(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first[required]")
        input1.send_keys("Anna")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second[required]")
        input2.send_keys("Salomonova")
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
        input3.send_keys("annasalomon@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first[required]")
        input1.send_keys("Anna")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second[required]")
        input2.send_keys("Salomonova")
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
        input3.send_keys("annasalomon@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)


if __name__ == "__main__":
    unittest.main()


