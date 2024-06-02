Feature: Online Shopping

Scenario: Search for a product, add it to the basket, and update the quantity
    Given I am an online shopper
    When I search for "monitor Asus" on Amazon
    And I add the first search result to my basket
    And I update the quantity of the item to "2"
    Then I should see "2" of the item in my basket
