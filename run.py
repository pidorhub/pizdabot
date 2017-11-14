import random_message
import config

import telebot

bot = telebot.TeleBot(config.get_token())
counter = 0


@bot.message_handler(commands=["pidor"])
def invoke_pidor_command(in_message):

    global counter
    counter += 1

    messages = random_message.get_messages()

    for message in messages:
        bot.send_message(in_message.chat.id, message)


@bot.message_handler(commands=["pidorstat"])
def invoke_stat_command(in_message):
    global counter
    message = 'Топ-10 пидоров за текущий год: \n \n' \
              '1. ApexNP — ' + str(counter) + '  раз(а)'
    bot.send_message(in_message.chat.id, message)


if __name__ == '__main__':
    bot.polling(none_stop=True)