Set-Location  "C:\Users\nn\BDD_SELENIUM_BEHAVE"
Start-Sleep 2
python3.11 -m behave  .\features\basic_menu.feature .\features\create_button.feature .\features\edit_button.feature .\features\return_button.feature .\features\table_content.feature .\features\video_element.feature .\features\slide_show.feature -f allure_behave.formatter:AllureFormatter -o Report_Json
Start-Sleep 2
allure generate Report_Json -o Report_Html --clean

