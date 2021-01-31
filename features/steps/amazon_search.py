from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')
# RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
# RESULTS = (By.XPATH, "//div[@class='g']")
#

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Watches into Amazon search field')
def input_amazon_search(context):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys('Watches')



    # THIS WILL ALWAYS BE USED WITH CONTEXT