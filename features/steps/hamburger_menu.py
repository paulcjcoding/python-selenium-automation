from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

HAM_MUNU = (By.ID, 'nav-hamburger-menu')

@then('Verify hamburger menu icon is visible')
def verify_has_menu_present(context):
    context.driver.find_element(*HAM_MUNU)

@when('Click to open Amazon Hamburger Menu')
def click_ham_menu(context):
    context.driver.find_element(*HAM_MENU).click()
    # context.driver.wait.until(EC)
    # driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
