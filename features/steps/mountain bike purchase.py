from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS = (By.XPATH, "//div[@class='g']")
ADD_TO_CART_BTN = (By.ID, 'submit.add-to-cart')
CART = (By.ID, 'nav-cart-count')
PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
INCLUDE_SERVICE_BTN = (By.ID, 'a-autoid-43-announce')

@given('Open Amazon page website')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Input Mountain Bike into Amazon search field')
def input_amazon_search(context):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys('Mountain Bike')

@when('Click on Amazon search icon link')
def click_search_amazon(context):
    search_icon = context.driver.find_element(By.ID, 'nav-search-submit-button')
    search_icon.click()

# @then('Product results for Mountain Bike are shown on Amazon')
# def verify_search_result(context):
#     actual_text = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
#     expected_text = '"Mountain Bike"'
#     assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_RESULT).click()

@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    if len(context.driver.find_elements(*SIZE_SELECTION_BTN)) == 1:
        context.driver.find_element(*SIZE_SELECTION_BTN).click()

@then('Verify cart has {expected_count} item')
def verify_url_contains_query(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} items but got {cart_count} items'