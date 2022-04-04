from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from gtts import gTTS

# import logging

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
#
# logger = logging.getLogger(__name__)

# Introduce the application
def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Beep boop! \n/bop for dog pics \n/mew for cats \n/meow for cat facts")


# bop for dog
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

def bop(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


# mew for cat
def cat_get_url():
    contents = requests.get('https://cataas.com/cat?json=true').json()
    extension = contents['url']
    url = "https://cataas.com" + extension
    return url

def mew(update, context):
    url = cat_get_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

# meow for cat fact
def meow(update, context):
    contents = requests.get('https://catfact.ninja/fact').json()
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=contents['fact'])

# secret function
def phew(update, context):
    text = "We will be okay, my love"
    output = gTTS(text=text, lang='en', slow=False)
    output.save('ouraudio.mp3')
    chat_id = update.message.chat_id
    context.bot.send_audio(chat_id=chat_id, audio=open('ouraudio.mp3', 'rb'))

# main function
def main():
    TOKEN = "1513084337:AAFFZClcaWO9TN1NFztkTP8xDM-4nQeBT64"
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('mew', mew))
    dp.add_handler(CommandHandler('meow', meow))
    dp.add_handler(CommandHandler('phew', phew))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
