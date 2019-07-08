import telebot
import config  # we connect config to take tokens

# We get Telegram token
bot = telebot.TeleBot(config.TOKEN_TELEGRAM)
print(bot.get_me())

