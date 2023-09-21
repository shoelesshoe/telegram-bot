import telegram
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def getApiKey():
    """Retrieves API Key from secrets.yaml (if already exists)

    If not, create the file and write the API Key given by the user's input"""
    global TOKEN

    try:
        with open('secrets.yaml', 'r') as f:
            TOKEN = f.read()
    except FileNotFoundError:
        userInput = input("Enter the bot's token: ")
        with open('secrets.yaml', 'w') as f:
            TOKEN = f.write(userInput)


async def start(update, context):
    """/start command

    test"""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="hi"
    )


if __name__ == '__main__':
    getApiKey()
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()