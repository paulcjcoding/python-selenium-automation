  # Created by Paul at 2/5/2021
Feature: Verify Shopping Cart is empty
  # Enter feature description here

  Scenario: Your Shopping Cart is empty
    Given Open Amazon page
    When Input {search_word} into search field
    Then Verify you can see Shopping Cart