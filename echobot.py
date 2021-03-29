import telegram
import os
from pprint import pprint

token = os.environ['token']
echobot = telegram.Bot(token=token)

echobot.sendMessage(1258594598, 'hi')