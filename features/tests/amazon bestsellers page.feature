# Created by Paul at 2/9/2021
Feature: Amazon Best Sellers tests
  # Enter feature description here

  Scenario: Amazon Best Sellers displays 5 links
    Given Open Amazon BestSellers page
    Then Verify 5 links are displayed
