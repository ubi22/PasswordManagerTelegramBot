import time

import telebot
from telebot import types
import hashlib

bot = telebot.TeleBot('6556863084:AAEmML03j4T2VDIZN8c0b2czKkP14XWcsyE')
password = "3dee4d4f4956ec6710b483cee5723b4d43e6ef7df57114f20f94d3d929ce2054"
authorization = False
time_authorization = 0
last_message_authorization = None
last_message_time_is_over = None
last_message = None
attempt = 0


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(message, 'Для начала авторизуйтесь')
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton(f"Авторизация")
    item2 = types.KeyboardButton("Посмотреть все записи")
    item3 = types.KeyboardButton("Добавить новую запись")
    markup.add(item1, item2, item3)


@bot.message_handler(commands=["Create_new_note"])
def see_note(message):
    if authorization:
        bot.send_message(message.chat.id, "Добавление новой записи")
    else:
        bot.send_message(message.chat.id, "Вы не авторизованы")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Авторизация":
        if authorization:
            bot.send_message(message.chat.id, "Вы уже вошли")
        else:
            bot.send_message(message.chat.id, "Введите пароль: ")
    # global authorization, last_message_authorization, last_message_time_is_over, last_message
    # if last_message_time_is_over:
    #     bot.delete_message(message.chat.id, last_message_time_is_over.message_id)
    #     last_message_time_is_over = None
    # if hashlib.sha256(message.text.encode()).hexdigest() == password:
    #     authorization = True
    #     last_message_authorization = bot.send_message(message.chat.id, "Вы вошли!!!", reply_markup=markup)
    #     print(last_message_time_is_over)
    #     while True:
    #         time.sleep(60)
    #         if time_authorization <= 5:
    #             authorization = False
    #             bot.delete_message(message.chat.id, last_message_authorization.message_id)
    #             last_message_time_is_over = bot.send_message(message.chat.id, "Время авторизации прошло\nВведите пароль:")
    #             break
    # elif last_message:
    #     bot.delete_message(message.chat.id, last_message.message_id)
    #     last_message = bot.send_message(message.chat.id, "Пароль неверный\nВведите пароль еще раз:")
    # else:
    #     last_message = bot.send_message(message.chat.id, "Пароль неверный\nВведите пароль еще раз:")
    #
    # bot.delete_message(message.chat.id, message.message_id)

bot.polling(none_stop=True)
