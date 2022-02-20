#!/bin/bash

source ./telegram.env
URL="https://api.telegram.org/bot$TOKEN/sendMessage"
curl -s -d "chat_id=$CHAT_ID&disable_web_page_preview=1&text=$1" $URL > /dev/null
