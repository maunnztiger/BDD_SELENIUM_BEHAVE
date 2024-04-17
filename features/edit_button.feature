Feature: Testing the edit-button functionality

Scenario: write a little test for the edit button
    GIVEN the user opens up the page "Men in Homeoffice Statistic"
    WHEN the user clicks on the edit button at the right end a row of the table
    THEN a popup opens up with the headline "Edit Row"
    AND the popup has a first label "Aspekt"
    AND the popup has a second label "Value"
    AND there is a "Save Changes"-Button below the editor-textfields
    AND there is 
