from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon page website for Watches')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Watches into Amazon search field')
def input_amazon_search(context):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys('Watches')

@when('Click on Amazon search icon link')
def click_search_amazon(context):
    search_icon = context.driver.find_element(By.ID, 'nav-search-submit-button')
    search_icon.click()

@then('Product results for Watches are shown on Amazon')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = '"Watches"'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Page URL has Watches in it')
def verify_url_contains_query(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = '"Watches"'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


    # THIS WILL ALWAYS BE USED WITH CONTEXT