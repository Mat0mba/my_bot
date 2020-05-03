import telebot
from telebot.types import Message
from time import sleep
from AsosCheckProduct import stock
from random import choice
from Weather import temp

bot = telebot.TeleBot("1223390742:AAEUd4e5twKYDViEkIsqU3eFLygvlpH4Cfg")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Чо умеешь?', 'Пока', "Тест: Любит/Не любит")
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Ля, попробуй', 'Ну тебя, узнай наличие джинсеков')


@bot.message_handler(commands=["start", "help"])
def send_message_welcome(message: Message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет, меня создал Колотил Данилов", reply_markup=keyboard1)
    elif message.text == "/help":
        bot.reply_to(message, "Помощи не жди, я бесполезный тестовый бот")

USERS = set()
@bot.message_handler(content_types=["sticker", "text"])
@bot.edited_message_handler(content_types=["text"])
def send_sticker(message: Message):
    USERS.add(message.from_user.id)
    if message.text.lower() == "чиллим?":
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMjXqwyrvOjawjmXMm3iTk9meFpVowAAogAAxZCawpb8KCh-HkAASUZBA")
    elif message.text.lower() == "чо умеешь?":
        if message.from_user.id in USERS:
            bot.reply_to(message, f"{message.from_user.first_name}, да ниче не умею толком, могу нахер послать", reply_markup=keyboard2)
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, "Бай")
    elif message.text.lower() == "ля, попробуй":
        bot.send_message(message.chat.id, "Пошел нахер чорт!")
    elif message.text.lower() == "ну тебя":
        bot.send_message(message.chat.id, "Как хочешь, похер, абсолютно")
        sleep(3)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMjXqwyrvOjawjmXMm3iTk9meFpVowAAogAAxZCawpb8KCh-HkAASUZBA")
    elif "наличие" in message.text.lower():
        InStock = stock()
        if InStock == False:
            bot.send_message(message.chat.id, "Сори, бро, их нет")
        else:
            bot.send_message(message.chat.id, "Беги забирать")
    elif "тест" in message.text.lower():
        result = choice(["Любит", "Не любит"])
        bot.send_message(message.chat.id, result)
    elif "погода" in message.text.lower():
        mas_city = message.text.split(" ")[1:]
        dots = " "
        city = dots.join(mas_city)
        try:
            temper = temp(city)
            bot.send_message(message.chat.id, f"Температура сейчас: {temper[0]}\nОщущается как: {temper[1]}\nПогодный статус: {temper[2]}")
        except:
            bot.send_message(message.chat.id, "Введи данные поточнее или исправь, пж")
    print(USERS)
bot.polling()




