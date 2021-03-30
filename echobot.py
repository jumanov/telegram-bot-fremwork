from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

TOKEN = '1747206956:AAG-ag4mlSeZWLNbmvj6BocrNThJ4puuI_g'

def command(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', command))

updater.start_polling()
updater.idle()