import telebot
import random
import time
import json
import types

token = "6291246526:AAFXd_JDTNOQfxuw__qMkpHqjH64hfzpE6Q"

bot = telebot.TeleBot(token)

f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton("Понедельник")
    item2 = telebot.types.KeyboardButton("Вторник")
    item3 = telebot.types.KeyboardButton("Среда")
    item4 = telebot.types.KeyboardButton("Четверг")
    item5 = telebot.types.KeyboardButton("Пятница")
    item6 = telebot.types.KeyboardButton("Суббота")
    item7 = telebot.types.KeyboardButton("Воскресенье")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, "План на неделю: ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    
    if message.text.lower() == "понедельник":
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('завтрак')
        item2 = telebot.types.KeyboardButton('обед')
        item3 = telebot.types.KeyboardButton('ужин')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'выбираем', reply_markup=markup)
        bot.register_next_step_handler(message)
    elif message.text.strip() == "вторник":
        ans = random.choice(facts)
    elif message.text.lower() == "среда":
        bot.send_message(message.chat.id, str(random.randint(1, 10)))
    elif message.text.lower() == "четверг":
        bot.send_message(message.chat.id, "понедельник")
    elif message.text.lower() == "пятница":
        bot.send_message(message.chat.id, str(random.randint()))
    elif message.text.lower() == "суббота":
        bot.send_message(message.chat.id, "выходной")
    elif message.text.lower() == "воскресенье":
        bot.send_message(message.chat.id, "выходной")
    else:
        bot.send_message(message.chat.id, "Я не знаю")
    bot.send_message(message.chat.id, ans)



bot.polling(none_stop=True)
