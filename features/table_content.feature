Feature: testing the content of a table

Scenario: write a simple test for the table-content of Homeoffice General Statistic
    GIVEN the title of the tab is "Homeoffice 2024" 
    WHEN the user clicks the menu-button in the left corner
    THEN there occurs a blue colored menu
    WHEN the user clicks on the menupoint "General Homeoffice Statistic"
    THEN a page opens with the headline "Homeoffice General Statistic"
    AND the page has a dropdown in the left corner with selected number of entries shown "50"
    AND in the right corner the page contains a search bar
    AND the page contains a dark blue colored button with the text "Go Back"
    AND the page contains another blue button with the text "Create Record"
    AND the page contains a table with "13" entries
    AND the table has "4" columns
    AND the first column has the title "Id"
    AND the second column has the title "Aspekt"
    AND the third column has the title "Value"
    AND the fourth column contains an edit button and a delete-button
    AND the first column rows have text-entries 
    AND the second column rows have text-entries 
    AND the third column rows have text-entries 
