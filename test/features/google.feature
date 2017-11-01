# -- FILE: features/google.feature
Feature: Search with Google
  As an information seeker,
  I want to search specific keyword on Google
  so that I can obtain related info.


  Scenario: Run a simple search
    Given I am on the Google TW page
     When I search 'AlphaGo'
     Then I can see many results.


  Scenario Outline: Run a series of simple searches
    Given I am on the Google TW page
     When I search '<keyword>'
     Then I can see many results.

    Examples: IaaS
     | keyword  |
     | Azure    |
     | AWS      |
     | GCP      | 

    Examples: Books
     | keyword               |
     | Harry Potter          |
     | The Lord of the Rings |


  Scenario: Run a simple search with browser
    Given I navigate the Google TW page
     When I summit with 'AlphaGo'
     Then I can see many results.
