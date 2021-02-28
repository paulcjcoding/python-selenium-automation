from multiprocessing import context
from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


DOG_IMG = (By.CSS_SELECTOR, "a[href='/dogsofamazon'] img")

@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@when('Click to open blog')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait(EC.new_window_is_opened)

@then('User can close new window and switch back to original')
def close_old_switch_to_new_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.origina_window)
    sleep(2)