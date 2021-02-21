from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.ID, "nav-cart-count")
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")
RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon help page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")


@when('Input the cancel order hit enter')
def input_search(context, search_word):
    search = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    click()
    sleep(4)


@then('Verify you can see cancel order')
def verify_url_contains_query(context):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'