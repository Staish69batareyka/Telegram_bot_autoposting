import telebot

bot = telebot.TeleBot('my token')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text:
        bot.send_message(message.from_user.id, "Hello world!")
