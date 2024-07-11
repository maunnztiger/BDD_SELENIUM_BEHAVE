Feature: Testing the create Button

Scenario: write a little test for the create-button functionality 
    GIVEN the title of the tab will still be "Homeoffice 2024" 
    WHEN the user clicks on the menu on the front page
    AND the user clicks on the menu-link "Men in Homeoffice Data"
    THEN the page "Men in Homeoffice Data" opens up again
    AND the title of the tab is again "Men in Homeoffice Data"
    WHEN the user clicks on the button "Create Record"
    THEN a Popup Window is openning up with the headline "Edit Row"
    AND there is a textfield with the label "Id:"
    AND there is a second textfield with the label "Aspekt:"
    AND there is a third textfield with the label "Value:"
    AND below the textfields there is a button "Create Record"
    AND there is a "Cancel" button 
    WHEN the user adds a Number that is 1 greater than last row ID to the Id-textfield
    AND adds the text-value "Männer, die kein Homeoffice machen wollen" to the Aspekt-textfield
    AND adds the percentage "2%" to the Value-textfield
    AND clicks on the Button "Create Record"
    THEN the Popup is no longer diplayed on the page
    AND after two seconds the new text-entry appears at the bottom of the table
    AND the last row "Id"-column has now new Id-text-entry
    AND the last row "Aspekt"-column has now the text-entry: "Männer, die kein Homeoffice machen wollen"
    AND the last row "Value"-column has now the text-entry: "2%"
    WHEN the user clicks on the trash-button on the right of the entry-row
    AND the user accepts the alert that is poping up
    THEN the according entry will be deleted from the table
