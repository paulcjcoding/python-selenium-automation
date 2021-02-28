# Created by Paul at 2/21/2021
Feature: Amazon Sign in tests
  # Enter feature description here

  Scenario: Sign in page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens

  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 5 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears

