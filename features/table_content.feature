Feature: testing the content of a table

Scenario Outline: write a simple test for the table-content of Homeoffice General Statistic
    GIVEN the title of the browser-tab is "Homeoffice 2024" 
    WHEN the user clicks the button in the left corner
    THEN there occurs a blue menu
    WHEN the user clicks on the menupoint "General Homeoffice Statistic"
    THEN a page opens with the headline "Homeoffice General Statistic"
    AND the page contains a table with 13 entries
    AND the table has three columns
    AND the first column is "Id"
    AND the second column is "Von den Befragten, die Homeoffice machen"
    AND the third column is "Wert in Prozent"
    AND the first cloumn in the first row has the text-entry "0"
    AND the second column in the first row has the text-entry "Angestellte in Deutschland, die 2020 die Chance auf Homeoffice hatten"
    AND the third column in the first row has the text-entry "36,0%"
    AND the first cloumn in the last row has the text-entry "12"
    AND the second column in the last row has the text-entry "Tatsächlich könnte ich meinen Job komplett aus dem Homeoffice machen"
    AND the third column in the last row has the text-entry "55,0%"