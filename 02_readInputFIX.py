import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = 'token'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="City and Regency Checker - Special Region of Yogyakarta",
    )

async def handle_menu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text

    regencies = ["Yogyakarta", "Sleman", "Gunungkidul", "Bantul", "Kulon Progo"]

    if user_choice in regencies:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Right! '"+ user_choice +"' is located in Special Region of Yogyakarta.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Wrong! Try again!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    menu_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu_choice)

    application.add_handler(start_handler)
    application.add_handler(menu_handler)

    application.run_polling()
