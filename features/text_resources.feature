Feature: Testing the text-resources feature

Scenario: write a little test for the the return-button functionality
    GIVEN the title of the tab is still "Homeoffice 2024" 
    WHEN the user clicks the menuButton on the front page
    AND the user clicks on the point "Text-Resourcen"
    THEN a page on the URL "http://192.168.178.53:5000/text_resources.html" opens up
    AND the page shows a dark blue field
    AND in the center of this blue field are two pictures below each other
    WHEN the user clicks on the upper picture 
    THEN the dark-blue field with the pictures dispappears
    AND an iframe opens up
    AND this iframe contains a text with a Homeoffice Report
    AND this Report has the title: "REPORT"
    WHEN the user clicks on the button "Text Menu" on the left top
    THEN the iframe dispappears
    AND there is the menu with the two pictures again
    WHEN the user clicks on the second picture below the upper picture
    THEN the same iframe opens up
    BUT this iframe contains an article with the headline "Hans Böckler Stiftung"
    WHEN the user clicks on the button "Text Menu" on the left
    THEN the iframe is disappered here
    AND the user returns to the menu with the two pictures which appears again
    WHEN the user clicks on the button "Main Menu" on the left top
    THEN the applications opens up the homepage again
    AND the headline of the page is "Homeoffice reporting tool"
    AND the title ob the tab is "Homeoffice 2024"
    AND the blue menu-field is closed
    BUT on the left corner there exists the button "Main Menu ☰"
    