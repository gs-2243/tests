import telebot
TOKEN = "1542453597:AAH7aa3nUnsdEfVmTEG-iKjDLQOHFPZeqd8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def echo(message: telebot.types.Message):
    bot.send_message(message.chat.id, "hello")

bot.polling()
