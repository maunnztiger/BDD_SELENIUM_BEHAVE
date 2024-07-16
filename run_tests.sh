#!/bin/bash
source ./venv/bin/activate
sleep 1
behave ./features/basic_menu.feature ./features/create_button.feature ./features/edit_button.feature ./features/return_button.feature ./features/table_content.feature ./features/video_element.feature  ./features/slide_show.feature -f allure_behave.formatter:AllureFo>sleep 1
allure generate Report_Json -o /home/igor/monitoring_tool/Report_Html --clean

