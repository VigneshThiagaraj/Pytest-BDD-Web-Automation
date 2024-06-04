Feature: Search any product in Amazon home page

  @smoke
  Scenario: Search a product and verify the search result
    When I enter the product name to be searched as "mobiles"
    Then I verify the search result