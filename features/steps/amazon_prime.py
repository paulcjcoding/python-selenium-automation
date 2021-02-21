from behave import when, then, given
from selenium.webdriver.common.by import By

BENEFIT_BOXES = (By.CSS_SELECTOR, '.benefit-box')

@given('Open Amazon Prime page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify 8 benefit boxes are displayed')
def verify_boxes(context):
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(actual_boxes) == 8, f'Expected 8 boxes, but we see {len(actual_boxes)}'



#Another way is the following:
# @then('Verify 8 benefit boxes are displayed')
# def verify_boxes(context):
#     actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
#       print(actual_boxes)
#     assert len(actual_boxes) == 8, f'Expected 8 boxes, but we see {len(actual_boxes)}'