import telegram
import os

token = os.environ['token']
echobot = telegram.Bot(token=token)
print(echobot.getMe(), '\n\n')
print(echobot.getMe().id)
print(echobot.getMe().username)
print(echobot.getMe().first_name)
print(echobot.getMe().last_name)
