from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/gp/help/customer/display.html")

driver.find_element(By.ID, "helpsearch").send_keys("International Shipping", Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//a[@class='a-link-normal']").text

expected_text = 'International Shipping'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()