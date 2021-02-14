# Created by Paul at 2/5/2021
Feature: # Cancelling an order on amazon
  # Enter feature description here

  Scenario: Cancel order
    Given Open Amazon help page
    When Input the cancel order hit enter
    And Verify you can see cancel order