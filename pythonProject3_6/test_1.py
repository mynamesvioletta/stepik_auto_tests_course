from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"


def test_login(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    log_but = browser.find_element(By.XPATH, "//a[@class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']")
    log_but.click()

    browser.implicitly_wait(5)
    email_inp = browser.find_element(By.XPATH, "//input[@type='email']")
    email_inp.send_keys("violettta.m28@gmail.com")

    browser.implicitly_wait(5)
    pass_inp = browser.find_element(By.XPATH, "//input[@type='password']")
    pass_inp.send_keys("Viola2014")

    browser.implicitly_wait(5)
    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()

time.sleep(5)