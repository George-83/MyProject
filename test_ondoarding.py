from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://open.spotify.com/"


def test_login():
    driver.get(url)
    driver.set_window_size(1200, 900)
    login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="login-button"]')
    login_button.click()
    time.sleep(2)
    input_login = driver.find_element(By.ID, 'login-username')
    input_password = driver.find_element(By.ID, 'login-password')
    submit_button = driver.find_element(By.ID, 'login-button')
    input_login.send_keys("")
    input_password.send_keys("")
    submit_button.click()
    time.sleep(3)
    account_icon = driver.find_element(By.CSS_SELECTOR, '[data-testid="placeholder-wrapper"]')
    assert account_icon is not None
    driver.close()
