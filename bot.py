import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'ok, start')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'what?')

print('bot running')
bot.polling()