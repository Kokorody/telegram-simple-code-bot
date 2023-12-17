import logging
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"Hi {user.first_name}! I'm thinking of a number between 1 and 100. Can you guess it?")

    context.user_data['number_to_guess'] = random.randint(1, 100)

def guess(update: Update, context: CallbackContext) -> None:
    user_guess = int(update.message.text)

    if 'number_to_guess' not in context.user_data:
        update.message.reply_text("Please start the game first using /start.")
        return

    number_to_guess = context.user_data['number_to_guess']

    if user_guess == number_to_guess:
        update.message.reply_text("Congratulations! You guessed the correct number.")
        del context.user_data['number_to_guess']
    elif user_guess < number_to_guess:
        update.message.reply_text("Try again. The number is higher.")
    else:
        update.message.reply_text("Try again. The number is lower.")

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I'm a game bot. Start the game using /start.")

def main() -> None:
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, guess))
    dispatcher.add_handler(MessageHandler(filters.command, echo))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
