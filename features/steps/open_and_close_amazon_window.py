from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TC = (By.XPATH, "//a[@href='https://www.amazon.com/gp/feature.html?docId=1000625601']")

# just for notes - (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")

@given ('Open Amazon T&C page')
def open_amazon_t_and_c_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle

@and('Click on Amazon applications link')
def click_on_amazon_app_link(context):
    context.driver.find_element(*TC).click()

@and('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.driver.switch_to.window(context.driver.window_handles[1])

@then('Amazon app page is opened')
def amazon_app_page_opened(context):
    sleep(10)

@and('User can close new window and switch back to original')
def close_new_window_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original.window)
    sleep(2)


