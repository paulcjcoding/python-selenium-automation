# Created by Paul at 2/9/2021
Feature: Amazon Prime tests
  # Enter feature description here

  Scenario: Amazon Prime displays 5 links
    Given Open Amazon BestSellers page
    Then Verify 5 links are displayed
