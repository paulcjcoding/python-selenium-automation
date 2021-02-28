from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
# driver.implicitly_wait(10) # 100 ms --- also to turn it off, set the # to 0
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# # wait for 4 sec
# sleep(4)
driver.wait = WebDriverWait(driver, 10)
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))   # another way to initiate is this way by adding the e = - this function will check every 500 ms
# Another way is by this way
# e = driver.wait.until(EC.((By.NAME, 'btnK')))   # another way to initiate is this way by adding the e = - this function will check every 500 ms
#Another common way/method
# e = driver.wait.until(EC.visibility_of_element_located((By.NAME, 'btnK')))   # another way to initiate is this way by adding the e = - this function will check every 500 ms


# click search
# driver.find_element(By.NAME, 'btnK').click()
e.click()   # another way to initiate is this way by adding the e = in the wait for 4 sec section (section above)

# verify
assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text

driver.quit()
