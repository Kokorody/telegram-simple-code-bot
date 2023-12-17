import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "your TOKEN"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a file, and I will convert its format for you.')

def convert_format(update: Update, context: CallbackContext) -> None:
    file_id = update.message.document.file_id
    new_format = "desired_format"

    file = context.bot.get_file(file_id)
    file_path = file.download()

    converted_path = convert_file(file_path, new_format)

    context.bot.send_document(update.message.chat_id, document=open(converted_path, 'rb'))

    os.remove(file_path)
    os.remove(converted_path)

def convert_file(file_path: str, new_format: str) -> str:
    pass

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, convert_format))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
