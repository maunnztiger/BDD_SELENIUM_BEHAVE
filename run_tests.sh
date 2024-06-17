#!/bin/bash
source ./venv/bin/activate
sleep 2
behave ./features/basic_menu.feature ./features/create_button.feature ./features/edit_button.feature ./features/return_button.feature ./features/table_content.feature ./features/video_element.feature
