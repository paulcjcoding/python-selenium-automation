from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

HAM_MUNU = (By.ID, 'nav-hamburger-menu')

@then('Verify hamburger menu icon is visible')
def verify_has_menu_present(context):
    context.driver.find_element(*HAM_MUNU)