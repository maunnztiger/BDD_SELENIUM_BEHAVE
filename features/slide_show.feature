Feature: Testing the slide show functionality

Scenario: Testing the slideshow functionality
    Given the user opens the frontpage's menu
    WHEN  the user clicks on the menu-point "Slideshows"
    THEN  another page opens up with the link "Was ist Remote Arbeit?"
    When  the user clicks on the link
    THEN  a new page opens up having the URL "http://www.dexterslab.com:8080/slide_1.html"  
    AND   there is a slideshow loaded with an image which has the aria-label "My Project-1.png"
    AND   the page has the number one "1"
    WHEN  the user clicks on the right-arrow on the right of the number 1
    THEN  a new slide-page with another image is loaded
    AND   the new image has the aria-label "My project-2.png"
    AND   the page has the number "2"
    WHEN  the user clicks on the left-arrow on the left of the number 2
    THEN  the first page with the first image is loaded again
    AND   the first page has the number "1"