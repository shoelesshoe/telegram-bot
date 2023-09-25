import logging
import bot

from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    # TELEGRAM
    bot.getTelegramApiKey()

    application = ApplicationBuilder().token(bot.TOKEN).build()
    
    start_handler = CommandHandler('start', bot.start)
    application.add_handler(start_handler)

    addEvent_handler = CommandHandler('addEvent', bot.addEvent)
    application.add_handler(addEvent_handler)
    
    application.run_polling()
