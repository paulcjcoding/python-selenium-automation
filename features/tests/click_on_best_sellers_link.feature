# Created by Paul at 2/25/2021
Feature: test for click on Best Sellers link
  # Enter feature description here

  Scenario: Amazon Best Sellers displays 5 links
    Given Open Amazon BestSellers page
    And Click on Best Sellers link
    And Switch to the newly opened window
    Then Best Seller page is opened
    And User can close new window and switch back to original

    And Click on New Releases link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original

    And Click on Movers & Shakers link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original

    And Click on Most Wished For link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original

    And Click on Gift Ideas link
    And Switch to the newly opened window
    Then Amazon app page is opened
    And User can close new window and switch back to original
