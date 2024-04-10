Feature: Testing the create Button

Scenario: write a little test for the create-button functionality 
    GIVEN the title of the tab is still "Homeoffice 2024" 
    WHEN the user clicks the menu-button on the front page
    AND the user clicks on the point "Men in Homeoffice Statistic"
    THEN the page "Homeoffice General Statistic" opens up
    AND the title of the tab is "Homeoffice General Statistic"
    WHEN the user clicks on the button "Create Record"
    THEN a Popup Window is openning up with the headline "Edit Row"
    AND there is a textfield with the label "Id:"
    AND there is a textfield with the label "Aspekt:"
    AND there is a textfield with the label "Value:"
    AND below the textfields there is a button "Create Record"
    AND there is a "Cancel" button 
    WHEN the user adds a Number that is 1 greater than last row ID to the Id-textfield
    AND adds the text-value "Männer, die unabhänging von Führungspositionen häufiger mobil arbeiten" to the Aspekt-textfield
    AND adds the percentage "54%" to the Value-textfield
    AND clicks on the Button "Create Record"
    THEN the Popup is no longer diplayed on the page
    AND after two seconds the new text-entry appears at the bottom of the table
    AND the last row "Id"-column has now text-entry: "5"
    AND the last row "Aspekt"-column has now the text-entry: "Männer, die unabhänging von Führungspositionen häufiger mobil arbeiten"
    AND the last row "Value"-column has now the text-entry: "54%"
