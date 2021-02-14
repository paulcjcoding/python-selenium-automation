# Created by Paul at 2/10/2021
Feature: Mountain Bike Purchase
  # Enter feature description here

  Scenario: User can add a product to the cart
    Given Open Amazon page website
    When Input Mountain Bike into Amazon search field
    When Click on Amazon search icon link
    Then Product results for Mountain Bike are shown on Amazon
    When Click on Add to cart button
    Then Verify cart has 1 item