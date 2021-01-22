# main.py
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from sightseer import Sightseer
from sightseer.zoo import YOLOv3Client

import logging
import os

telegram_bot_token = "YOUR-TOKEN-Here"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please send me a picture and I will try to tell you what's in it.")


def downloadImage(update, context):
    downloaded_path = "img"
    file_id = update.message.photo[-1].file_id
    file_unique_id = update.message.photo[-1].file_unique_id

    new_file= context.bot.get_file(file_id)
    saving_path= os.path.join(downloaded_path, "{}.jpg".format(file_unique_id))
    new_file.download(saving_path)

    yolo = YOLOv3Client()
    yolo.load_model() # downloads weights

    # loading image from local system
    ss = Sightseer()
    image = ss.load_image(saving_path)
    
    preds, pred_img = yolo.predict(image, return_img=True)

    itemsStrings = ""
    for items in preds:
        itemsStrings += str(items[0]) + ": " + str(items[1]) + "\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=itemsStrings)


downloadImage_handler = MessageHandler(Filters.photo & (~Filters.command), downloadImage)
dispatcher.add_handler(downloadImage_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()