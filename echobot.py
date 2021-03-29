import telegram
import os
from pprint import pprint

token = os.environ['token']
echobot = telegram.Bot(token=token)

pprint(echobot.getUpdates()[0])