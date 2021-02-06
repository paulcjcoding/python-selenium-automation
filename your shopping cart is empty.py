from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")

driver.find_element(By.ID, "nav-cart-count").click()

actual_text = driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
expected_text = 'Your Amazon Cart is empty'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()


