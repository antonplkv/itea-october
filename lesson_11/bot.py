from config import TOKEN
from telebot import TeleBot
import random

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    print(message)
    bot.send_message(
        message.chat.id,
        'Hello!'
    )


@bot.message_handler(func=lambda m: m.text in {'Привет', 'Хай', 'Салют'})
def handle_hello(message):
    greetings = ['Hola', 'Hello', 'Hi', 'Здравствуй']
    bot.send_message(
        message.chat.id,
        random.choice(greetings)
    )


@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = f'Ты написал мне следующее: {message.text}'
    bot.send_message(
        message.chat.id,
        text
    )


@bot.message_handler(commands=['whoami'])
def handle_whoami(message):
    user_info = f'Твоё имя: {message.from_user.first_name}\n' \
                f'Никнейм: @{message.from_user.username}\nid: {message.from_user.id}'
    bot.send_message(message.chat.id, user_info)


# import time
# for i in range(10):
#     bot.send_message(392635953, 'Привет')
#     time.sleep(0.5)

bot.polling()