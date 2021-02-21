# Created by Paul at 2/7/2021
Feature: Amazon Prime tests
  # Enter feature description here

  Scenario: Amazon Prime displays 8 benefit boxes
    Given Open Amazon Prime page
    Then Verify 8 benefit boxes are displayed