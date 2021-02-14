# Created by Paul at 1/24/2021
Feature: Amazon Search Test
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page website for Watches
    When Input Watches into Amazon search field for Watches
    When Click on Amazon search icon
    And Click on Amazon search icon
    Then Product results for Watches are shown on Amazon