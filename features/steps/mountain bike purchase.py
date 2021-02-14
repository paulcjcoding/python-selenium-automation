from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS = (By.XPATH, "//div[@class='g']")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')


@given('Open Amazon page website')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Mountain Bike into Amazon search field')
def input_amazon_search(context):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys('Mountain Bike')

@when('Click on Amazon search icon')
def click_search_amazon(context):
    search_icon = context.driver.find_element(By.ID, 'nav-search-submit-button')
    search_icon.click()

@then('Product results for Mountain Bike are shown on Amazon')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = '"Mountain Bike"'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@when('Click on Add to cart button')
def click_search_amazon(context):
    search_icon = context.driver.find_element(By.ID, 'nav-search-submit-button')
    search_icon.click()

@then('Verify cart has 1 item')
def verify_url_contains_query(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    expected_text = '"Mountain Bike"'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'