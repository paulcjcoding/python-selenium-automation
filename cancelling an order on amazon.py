from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/gp/help/customer/display.html")

driver.find_element(By.ID, "helpsearch").send_keys("Cancel Items or Orders", Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()