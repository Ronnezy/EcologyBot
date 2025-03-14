import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start_bot_message(message):
    bot.reply_to(message, 'Привет! Вы используете Бот Экологии. Для того, чтобы узнать список команд введите команду "/help"')

@bot.message_handler(commands=['help'])
def help_command(message):
    f = open('commandsList.txt', 'r', encoding='utf-8')

    bot.reply_to(message, f.read())

@bot.message_handler(commands=['SortedRules'])
def SortedRules(message):
    sorted_rules_file = open('SortedRules.txt', 'r', encoding='utf-8')

    bot.reply_to(message, sorted_rules_file.read())

@bot.message_handler(commands=['AlternativesItems'])
def alternatives_items(message):
    alternatives_items_file = open('AlternativesItems.txt', 'r', encoding='utf-8')

    bot.reply_to(message, alternatives_items_file.read())

@bot.message_handler(commands=['AboutEcology'])
def about_ecology(message):
    about_ecology_file = open('AboutEcology.txt', 'r', encoding='utf-8')

    bot.reply_to(message, about_ecology_file.read())

@bot.message_handler(commands=['RulesForUsingPlastic'])
def rules_for_using_plastic(message):
    rules_file = open('RulesForUsingPlastic.txt', 'r', encoding='utf-8')

    bot.reply_to(message, rules_file.read())

@bot.message_handler(commands=['TransportForSaveEcology'])
def transport(message):
    transport_file = open('TransportForSaveEcology.txt', 'r', encoding='utf-8')

    bot.reply_to(message, transport_file.read())

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
