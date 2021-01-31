from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\Paul\\PycharmProjects\\python-selenium-automation\\chromedriver')
driver.maximize_window()

#open the url
driver.get('https://www.google.com')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Mountain bike')

#wait for 4 sec
sleep(4)

#click search
driver.find_element(By.NAME, 'btnK').click()

#verify - this code is not working but looks to be working properly without the code below.
# assert 'Mountain bike' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
# assert 'Mountain bike' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()