# Created by Paul at 2/27/2021
Feature: tests for 404 page
  # Enter feature description here

  Scenario: Amazon 404 page opens blog in another window
    Given Open Amazon Dress B0777K16R9V3 page
    When Store original windows
    And Click to open blog
    And Switch to the newly opened window
#    Then User can close new window and switch back to original