Feature: Testing the video feature of the page

Scenario:   Testing the video feature
    Given   the user opens the frontpage's menu
    WHEN    the user clicks on the button "Homeoffice: Video Statements"
    THEN    a new page with a list of 7 embedded Youtube-videos opens up
    AND     the page has the tab-title "Remote from Gitlab"
    WHEN    the user clicks on the red play-button on of the videos
    THEN    the video is played
    WHEN    the user presses "k"-key on the keyboard
    THEN    the video is paused      