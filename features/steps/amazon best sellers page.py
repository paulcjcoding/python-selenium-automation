from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
RESULTS = (By.XPATH, "//div[@class='g']")


@given('Open Amazon BestSellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Product results show link for Best Sellers')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')]").text
    expected_text = 'Best Sellers'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Product results show link for New Releases')
def verify_url_contains_query(context):
    actual_text = context.driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/new-releases/ref=zg_bs_tab')]").text
    expected_text = 'New Releases'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Product results show link for Movers & Shakers')
def verify_url_contains_query(context):
    actual_text = context.driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/movers-and-shakers/ref=zg_bs_tab')]").text
    expected_text = 'Movers & Shakers'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Product results show link for Most Wished For')
def verify_url_contains_query(context):
    actual_text = context.driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/most-wished-for/ref=zg_bs_tab')]").text
    expected_text = 'Most Wished For'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

@then('Product results show link for Gift Ideas')
def verify_url_contains_query(context):
    actual_text = context.driver.find_element(By.XPATH, "//a[contains(@href, 'https://www.amazon.com/gp/most-gifted/ref=zg_bs_tab')]").text
    expected_text = 'Gift Ideas'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'






    # THIS WILL ALWAYS BE USED WITH CONTEXT