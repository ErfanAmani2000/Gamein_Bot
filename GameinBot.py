import telebot


bot = telebot.TeleBot("5720243463:AAGrEUh88NsF7aJ3w3cxPMxPEfSkxaGrEf0")


@bot.message_handler(commands=['Hello'])
def welcome(message):
    bot.reply_to(message, 'Welcome to Gamein 2022')


bot.polling()


class Player:
    def __init__(self):
        pass

    def purchase_raw_material(self):
        pass

    def produce(self):
        pass


class Gamein(Player):
    def __init__(self):
        super().__init__()

    def sale_raw_material(self):
        pass

    def purchase_form_player(self):
        pass
