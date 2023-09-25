def getTelegramApiKey():
    """Retrieves Telegram API Key from secrets.txt (if already exists)

    If not, create the file and write the API Key given by the user's input"""
    global TOKEN

    try:
        with open('./credentials/secrets.txt', 'r') as f:
            TOKEN = f.read()
    except FileNotFoundError:
        userInput = input("Enter the bot's token: ")
        with open('./credentials/secrets.txt', 'w') as f:
            TOKEN = f.write(userInput)


async def start(update, context):
    """/start command

    test"""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="hi"
    )


async def addEvent(update, context):
    global msg
    msg = update.message.text