from behave import when, then, given
from selenium.webdriver.common.by import By

FIVE_LINKS = (By.CSS_SELECTOR, '#zg_tabs li')

@given('Open Amazon BestSellers page')
def open_prime(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers_22595f4f23134e4aa687cca616dd2701')


@then('Verify 5 links are displayed')
def verify_boxes(context):
    actual_links = context.driver.find_elements(*FIVE_LINKS)
    assert len(actual_links) == 5, f'Expected 5 links, but we see {len(actual_links)}'