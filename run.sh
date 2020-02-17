#!/bin/sh
python3 weibo.py

export https_proxy=http://127.0.0.1:8118
python3 tgbot.py
export https_proxy=

head -n 3 config.json > config.json.swp
echo '    "since_date": "'$(date +%Y-%m-%d)'",' >> config.json.swp
tail -n 6 config.json >> config.json.swp
rm config.json
mv config.json.swp config.json
