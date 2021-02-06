# Created by Paul at 2/5/2021
Feature: # Verify Shopping Cart is empty
  # Enter feature description here

  Scenario: # Your Shopping Cart is empty
   Given Open Amazon help page
    When Input the cancel order hit enter
    And Verify you can see cancel order


  Scenario: Cancel order
    Given Open Amazon help page
    When Input the cancel order hit enter
    And Verify you can see cancel order