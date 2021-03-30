import telegram
import os
from pprint import pprint

token = os.environ['token']
echobot = telegram.Bot(token=token)
update_id0 = 0
while True:
    data = echobot.getUpdates()[-1]
    chat_id = data.message.chat.id
    text = data.message.text
    update_id1 = data.update_id
    if update_id0 != update_id1:
        echobot.sendMessage(chat_id, text)
        update_id0 = update_id1