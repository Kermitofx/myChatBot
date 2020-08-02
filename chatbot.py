import os
import telebot
import aiml

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá, bem vindo ao nosso botinho")
    

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Em que podemos ajudar você?")

@bot.message_handler(commands=['sair'])
def send_exit(message):
    bot.reply_to(message, "Obrigad@, ficamos felizes em ajudar você")

@bot.message_handler(commands=['menu'])
def send_menu(message):
    bot_ia = aiml.Kernel()
    bot_ia.learn('./files_XML/menu.xml')
    saida = bot_ia.respond(message.text)
    bot.reply_to(message, saida)

@bot.message_handler(func=lambda m: True)
def converse(message):
    bot_ia = aiml.Kernel()
    bot_ia.learn('./files_XML/bot-enfase.xml')
    saída = bot_ia.respond(message.text)
    bot.reply_to(message, saída)
     # bot.reply_to(message, 'OI')

bot.polling()
