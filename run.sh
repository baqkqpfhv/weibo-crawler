python3 weibo.py
python3 tgbot.py

head -n 3 config.json > config.json.swp
echo '    "since_date": "'$(date +%Y-%m-%d)'",' >> config.json.swp
tail -n 6 config.json >> config.json.swp
rm config.json
mv config.json.swp config.json
