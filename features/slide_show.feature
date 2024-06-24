Feature: Testing the slide show functionality

Scenario: Testing the slideshow functionality
    Given the user opens the frontpage's menu
    WHEN  the user clicks on the menu-point "Slideshows"
    THEN  another page opens up with the link "Was ist Remote Arbeit?"
    When  the user clicks on the link
    THEN  a new page opens up having the URL "http://192.168.178.53:8080/slide_1.html"  
    AND   there is a slideshow loaded with an image which has the aria-label "My project-1.png"
    AND   the page has the number "1"
    WHEN  the user clicks on the right-arrow on the right of the number 1
    THEN  a new slide-page with new image has the aria-label "My project-2.png"
    AND   the page shows number "2"
    WHEN  the user clicks on the left-arrow on the left of the number 2
    THEN  the first page with the first image with the aria-label "My project-1.png" is loaded again
    AND   the first page shows the number "1"

    