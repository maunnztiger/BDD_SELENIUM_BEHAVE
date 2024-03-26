Feature: writing tests for the dexterslab basic functions

Scenario: run a simple test
   GIVEN the title of the browser-tab is "Homeoffice 2024" 
   WHEN the user clicks the button in the left corner
   THEN there occurs a blue menu
   AND the first menu-point is: "Homeoffice General Statistic"
   AND the second menu-point is: "Men in Homeoffice Statistic"
   AND the third menu-point is: "Homeoffice Special Statistic"
   AND the fourth menu-point is: "Advantages of Homeoffice"
   AND the fifth menu-point is: "Disadvantages of Homeoffice"
   AND the sixth menu-point is: "Homeoffice compared with Europe"
   WHEN the user clicks the button in the left corner
   THEN the menu dissapears again
   