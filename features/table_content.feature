Feature: testing the content of a table

Scenario Outline: write a simple test for the table-content of Homeoffice General Statistic
    GIVEN the title of the browser-tab is "Homeoffice 2024" 
    WHEN the user clicks the menu-button in the left corner
    THEN there occurs a blue menu
    WHEN the user clicks on the menupoint "General Homeoffice Statistic"
    THEN a page opens with the headline "Homeoffice General Statistic"
    AND the page has a dropdown in the left corner with selected number of entries shown "50"
    AND in the right corner the page contains a search bar
    AND the page contains a dark blue colored button with the text "Go Back"
    AND the page contains another blue button with the text "Create Record"
    AND the page contains a table with 13 entries
    AND the table has four columns
    AND the first column has the title "Id"
    AND the second column has the title "Aspekt"
    AND the third column has the title "Value"
    AND the fourth column contains an edit button and a delete-button
    AND the first cloumn in the row has the text-entry "<Id>"
    AND the second cloumn in the row has the text-entry "<Aspekt>"
    AND the third cloumn in the row has the text-entry "<Value>"

    
    Examples:

        | Id    | Aspekt                                                                        | Value           |
        | 0     | Angestellte in Deutschland, die 2020 die Chance auf Homeoffice hatten         | 36,0%           |
        | 1     | Männer arbeiten öfter an einem nicht festgelegeten Arbeitsplatz als Frauen    | 11,5%           |
        | 2     | Angestellte im Homeoffice, die einen Büro-Vollzeit-Job haben                  | 70,0%           |
        | 3	    | Europaweiter Vergleich der Homeoffice-Möglichkeit in Deutschland              | 5,0%   	      |
        | 4	    | Luxemburg: Anteil der Angestellten mit Remote-Arbeit	                        | 53,4%  	      |
        | 5 	| Wegfall des Arbeitswegs als größter Vorteil                                   | 76,0%		      |
        | 6	    | Vereinbarkeit von Beruf und Familie als Vorteil	                            | 73,0%	          |
        | 7	    | Nachteilig der fehlende Kontakt zu Kollegen	                                | 74,0%		      |
        | 8	    | Nachteilig die unklare Trennung von Beruf und Privatleben                     | 45,0%		      |
        | 9	    | Wollen auch nach Corona eine Möglichkeit auf Homeoffice	                    | 48,0%		      |
        | 10	| Befürworten ein gesetzliches Recht auf Homeoffice                             | 73,0%		      |
        | 11    | Von allen Berufstätigen während Corona im Homeoffice                          | 45,0%		      |
        | 12    | Tatsächlich könnte ich meinen Job komplett aus dem Homeoffice machen          | 55,0%           |