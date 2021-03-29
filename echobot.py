import telegram
import os

token = os.environ['token']
echobot = telegram.Bot(token=token)
print(echobot.getMe().id)
