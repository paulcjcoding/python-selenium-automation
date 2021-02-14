# Created by Paul at 2/9/2021
Feature: Amazon BestSellers page
  # Enter feature description here

  Scenario: User can verify there are 5 links
    Given Open Amazon BestSellers page
    Then Product results show link for Best Sellers
    Then Product results show link for New Releases
    Then Product results show link for Movers & Shakers
    Then Product results show link for Most Wished For
    Then Product results show link for Gift Ideas