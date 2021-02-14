from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")

# driver.find_element(By.ID, "zg_tabs").send_keys("Cancel Items or Orders", Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')]").text
expected_text = 'Best Sellers'

actual_text = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/new-releases/ref=zg_bs_tab')]").text
expected_text = 'New Releases'

actual_text = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/movers-and-shakers/ref=zg_bs_tab')]").text
expected_text = 'Movers & Shakers'

actual_text = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/most-wished-for/ref=zg_bs_tab')]").text
expected_text = 'Most Wished For'

actual_text = driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/most-gifted/ref=zg_bs_tab')]").text
expected_text = 'Gift Ideas'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()



# actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
# expected_text = 'New Releases'
