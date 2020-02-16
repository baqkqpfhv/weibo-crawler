#!/usr/bin/env python3

import json
import telegram

JSON_FILE = 'weibo/广州天气/2294193132.json'
TEXT_ID_FILE = 'tgbot_config/text_id.txt'
CHAT_ID_FILE = 'tgbot_config/chat_id.txt'
TOKEN_FILE = 'tgbot_config/bot_token.txt'

WEIBO_TEXT_LINK_PREFIXES = 'https://m.weibo.cn/detail/'

text_id = 0
chat_id = 0

def get_text_id():
	global text_id
	with open(TEXT_ID_FILE, 'r') as file:
		text_id = int(file.read())

def get_chat_id():
	global chat_id
	with open(CHAT_ID_FILE, 'r') as file:
		chat_id = int(file.read())

def get_token():
	with open(TOKEN_FILE, 'r') as file:
		token = file.read()[:-1]
	return token

bot = telegram.Bot(token=get_token())

def set_text_id():
	file = open(TEXT_ID_FILE, 'w')
	file.write(str(text_id))
	file.close()

def send_message(text):
	weibo_text = text["text"]
	weibo_text_link = WEIBO_TEXT_LINK_PREFIXES + str(text["id"])
	print(weibo_text)
	print(weibo_text_link)
	bot.send_message(chat_id = chat_id,
			#text = weibo_text + 
			text = 
			'(<a href="' + weibo_text_link + '">广州天气</a>.)',
			parse_mode = telegram.ParseMode.HTML,
			disable_web_page_preview=True)

def decode_data():
	global text_id
	with open(JSON_FILE, 'r') as file:
		data = json.loads(file.read())
	weibo = data['weibo']
	current_max_text_id = text_id
	for text in weibo:
		if text["id"] > text_id:
			send_message(text)
			current_max_text_id = max(current_max_text_id, text["id"])
	text_id = current_max_text_id

get_text_id()
get_chat_id()
decode_data()
#set_text_id()
