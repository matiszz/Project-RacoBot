from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging

updater = Updater(token="651324863:AAHFpPhxnJSisqWidTlfU9MrgQ8P-uLTJ6s")
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola, como estás?")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    textCaps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=textCaps)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Lo siento, no he entendido el comando.")

def setRacoToken(self, token):
    racoToken = token

startHandler = CommandHandler('start', start)
capsHandler = CommandHandler('caps', caps, pass_args=True)
echoHandler = MessageHandler(Filters.text, echo)
unknownHandler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(startHandler)
dispatcher.add_handler(capsHandler)
dispatcher.add_handler(echoHandler)
dispatcher.add_handler(unknownHandler)

updater.start_polling()
