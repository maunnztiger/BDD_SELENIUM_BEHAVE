Feature: Testing the return buttons feature

Scenario: write a little test for the the return-button functionality
    GIVEN the title of the tab is still "Homeoffice 2024" 
    WHEN the user clicks the menu-button on the front page
    AND the user clicks on the menupoint "Men in Homeoffice Statistic"
    THEN the page "Men in Homeoffice Statistic" opens up
    AND the title of the tab is "Men in Homeoffice Statistic"
    WHEN the user clicks on the dark blue Button "Go Back"
    THEN the front page with the headline "Homeoffice reporting tool" appears again
    AND the title of the tab is again "Homeoffice 2024" 

