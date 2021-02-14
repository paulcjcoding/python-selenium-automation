from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#
# # Created by Paul at 2/5/2021
# Feature: Verify Shopping Cart is empty
#   # Enter feature description here
#
# Scenario: Your Shopping Cart is empty
#     Given Open Amazon page
#     When Click on shopping cart icon
#     Then Verify you can see Shopping Cart is empty


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.ID, "nav-cart-count")
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")
RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    click()
    sleep(4)

# driver.find_element(By.ID, "nav-cart-count").click()


@then('Verify you can see Shopping Cart is empty {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
