import datetime
import telebot
import requests
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
from telethon import functions, types
api_id=''
api_hash=''
api_name='@'
#message='WorkingPyTele'
message=input('Enter your message: ')
phone=input('Enter the phone with code: ')
client = TelegramClient('session', api_id, api_hash)
client.connect()
#client.send_message('me', 'Hello to myself!')
# first time ask either to input token or otp sent to number or sent or your telegram id
if not client.is_user_authorized():
	client.send_code_request(phone)
	client.sign_in(phone, input('Enter the code: '))
client.send_message('channelname', message, parse_mode='html')
#try:
#	receiver = InputPeerUser(api_id, api_hash)
#	print(receiver,message)
#	client.send_message(receiver, message, parse_mode='html')
#except Exception as e:
#	# there may be many error coming in while like peer
#	# error, wrong access_hash, flood_error, etc
#	print(e)
# disconnecting the telegram session
client.disconnect()