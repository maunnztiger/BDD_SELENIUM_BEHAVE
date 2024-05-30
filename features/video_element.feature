Feature: Testing the video feature of the page

Scenario:   Testing the video feature
    Given   the user opens the frontpage's menu
    WHEN    the user clicks on the button "Homeoffice: Video Statements"
    THEN    a new page with the headline "Video List" opens up
    AND     this page has a list of "7" links to certain videos
    AND     the page has the tab-title "Remote from Gitlab"
    WHEN    the user clicks on one of the video-links
    THEN    a new page with the according embedded Video opens up
    WHEN    the user clicks on the red play-button on the video
    THEN    the video is played
    WHEN    the user presses "k"-key on the keyboard
    THEN    the video is paused
    WHEN    the user clicks on the button "Video Menu ☰" on the left top of the page
    THEN    the page with the headline "Video List" opens up again
    WHEN    the user activates the button "Main Menu ☰" on the left top of the page
    THEN    the frontpage of the app is opened up with the headline "Homeoffice reporting tool"     