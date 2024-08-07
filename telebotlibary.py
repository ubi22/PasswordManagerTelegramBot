import telebot
from telebot import types
import hashlib
bot = telebot.TeleBot('6556863084:AAEmML03j4T2VDIZN8c0b2czKkP14XWcsyE')
password = "3dee4d4f4956ec6710b483cee5723b4d43e6ef7df57114f20f94d3d929ce2054"


@bot.message_handler(commands=['start','help'])
def handle_start(message):
  bot.reply_to(message, 'Введите пароль:')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print(type(message.text))
    print(hashlib.sha256(message.text.encode()).hexdigest(), "==", password)
    if hashlib.sha256(message.text.encode()).hexdigest() == password:
        bot.send_message(message.chat.id, "Вы вошли!!!")
    else:
        bot.reply_to(message, "Пароль неверный")

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,"Введите пароль: ")
#
#
# @bot.message_handler(content_types='text')
# def message_reply(message):
#

bot.polling(none_stop=True)