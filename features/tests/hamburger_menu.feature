# Created by Paul at 2/14/2021
Feature: # Tests for Amazon Hamburger Menu
  # Enter feature description here

  Scenario: User sees Amazon Hamburger Menu icon
    Given Open Amazon page
    Then Verify hamburger menu icon is visible
    When Click to open Amazon Hamburger Menu