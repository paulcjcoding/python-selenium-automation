from behave import when, then, given
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BEST_SELLERS = (By.XPATH, "//a[contains(@href, 'https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')]")
# NEW_RELEASES = (By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/new-releases/ref=zg_bs_tab')]")
# MOVERS_AND_SHAKERS = (By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/most-wished-for/ref=zg_bs_tab')]")
# MOST_WISHED_FOR = (By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/most-wished-for/ref=zg_bs_tab')]")
# GIFT_IDEAS = (By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/most-gifted/ref=zg_bs_tab')]")

#*******************TRYING ANOTHER WAY******************
BEST_SELLERS = (By.XPATH, "//*[contains(@href='https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')]")
NEW_RELEASES = (By.XPATH, "//*[contains(@href='https://www.amazon.com/gp/new-releases/ref=zg_bs_tab')]")
MOVERS_AND_SHAKERS = (By.XPATH, "//*[contains(@href='https://www.amazon.com/gp/most-wished-for/ref=zg_bs_tab')]")
MOST_WISHED_FOR = (By.XPATH, "//*[contains(@href='https://www.amazon.com/gp/most-wished-for/ref=zg_bs_tab')]")
GIFT_IDEAS = (By.XPATH, "//*[contains(@href='https://www.amazon.com/gp/most-gifted/ref=zg_bs_tab')]")

# "//*[@href='https://www.amazon.com/gp/feature.html?docId=1000625601']")

@given ('Open Amazon Best Sellers page')
def open_amazon_bestseller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers_22595f4f23134e4aa687cca616dd2701')

@and('Click on Best Sellers link')
def click_on_amazon_app_link(context):
    context.driver.find_element(*BEST_SELLERS).click()

@and('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Best Seller page is opened')
def amazon_app_page_opened(context):
    sleep(10)

@and('User can close new window and switch back to original')
def close_new_window_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original.window)
    sleep(2)

#*********NEW-RELEASES

@and('Click on New Releases link')
def click_on_amazon_app_link(context):
    context.driver.find_element(*NEW_RELEASES).click()

@and('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Best Seller page is opened')
def amazon_app_page_opened(context):
    sleep(10)

@and('User can close new window and switch back to original')
def close_new_window_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original.window)
    sleep(2)

#*********** MOVERS & SHAKERS

@and('Click on Movers & Shakers link')
def click_on_amazon_app_link(context):
    context.driver.find_element(*MOVERS_AND_SHAKERS).click()

@and('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Best Seller page is opened')
def amazon_app_page_opened(context):
    sleep(10)

@and('User can close new window and switch back to original')
def close_new_window_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original.window)
    sleep(2)

#*************MOST WISHED FOR

@and('Click on Most Wished For link')
def click_on_amazon_app_link(context):
    context.driver.find_element(*MOST_WISHED_FOR).click()

@and('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Best Seller page is opened')
def amazon_app_page_opened(context):
    sleep(10)

@and('User can close new window and switch back to original')
def close_new_window_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original.window)
    sleep(2)

#****************GIFT IDEAS

@and('Click on Gift Ideas link')
def click_on_amazon_app_link(context):
    context.driver.find_element(*GIFT_IDEAS).click()

@and('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Best Seller page is opened')
def amazon_app_page_opened(context):
    sleep(10)

@and('User can close new window and switch back to original')
def close_new_window_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original.window)
    sleep(2)