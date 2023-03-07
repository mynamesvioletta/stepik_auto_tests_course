import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


@pytest.mark.parametrize('url', ["236895",
                                 "236896",
                                 "236897",
                                 "236898",
                                 "236899",
                                 "236903",
                                 "236904",
                                 "236905"])

def test_login(browser, url):
    browser.implicitly_wait(5)
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)

    log_but = browser.find_element(By.XPATH, "//a[@class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']")
    log_but.click()

    browser.implicitly_wait(5)
    email_inp = browser.find_element(By.XPATH, "//input[@type='email']")
    email_inp.send_keys("violettta.m28@gmail.com")

    pass_inp = browser.find_element(By.XPATH, "//input[@type='password']")
    pass_inp.send_keys("Viola2014")

    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    time.sleep(10)

    ans = browser.find_element(By.XPATH, "//textarea[@class='ember-text-area ember-view textarea string-quiz__textarea']")
    ans.send_keys(str(math.log(int(time.time() + 0.5))))

    ans_but = browser.find_element(By.XPATH, "//button[@class='submit-submission']")
    ans_but.click()

    ans_text = browser.find_element(By.XPATH, "//div[@class='smart-hints ember-view lesson__hint']/p[@class='smart-hints__hint']")

    assert (ans_text.text == "Correct!"), f"LALALALLALAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

