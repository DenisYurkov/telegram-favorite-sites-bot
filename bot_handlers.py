from bot import *  # Import bot object
from messages import *  # Import everything from the message file

# We send bot greetings
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, START_MESSAGE)
    bot.reply_to(message, HELP_MESSAGE)


# Handles all text messages that match the regular expression
@bot.message_handler(regexp="/sites")
def handle_message(message):
    if "/sites":
        bot.reply_to(message, MY_SITE_PORTFOLIO)
        bot.reply_to(message, MY_GITHUB_ACCOUNT)
        bot.reply_to(message, GOOGLE)
        bot.reply_to(message, STACKOVERFLOW)
        bot.reply_to(message, VK)
        bot.reply_to(message, FACEBOOK)
        bot.reply_to(message, GOOGLE_TRANSLATE)
        bot.reply_to(message, GITHUB)
        bot.reply_to(message, PYTHON)
        bot.reply_to(message, REDDIT)
        bot.reply_to(message, YOUTUBE)


# If the message is not /sites then output the message to enter /sites
@bot.message_handler(content_types='text')
def other_word(message):
    bot.reply_to(message, ERROR_MESSAGE)


# The bot works without stopping
if __name__ == "__main__":        
	bot.polling(none_stop=True)

