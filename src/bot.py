import re
import datefinder

from telegram import Update
from telegram.ext import ContextTypes


def getTelegramApiKey() -> None:
    """Retrieves Telegram API Key from secrets.txt (if already exists)

    If not, create the file and write the API Key given by the user's input"""
    global TOKEN

    try:
        with open('./credentials/telegram_key.txt', 'r') as f:
            TOKEN = f.read()
    except FileNotFoundError:
        while True:
            TOKEN = input("Enter the bot's token: ")
            check = input("Are you sure you have keyed in the correct token? Enter y/n: ")
            if check == 'y':
                break
        with open('./credentials/telegram_key.txt', 'w') as f:
            f.write(TOKEN)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start command

    test"""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="hi"
    )


async def addEvent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/addEvent command
    
    adds a Google Calendar event"""
    cmd = len('/addEvent ')
    msg = update.message.text[cmd:]

    # examples of inputs:
    # bdmt @ beatty 23 sep 5pm-8pm
    # eventname     date   time

    # john bday every       26 oct 
    # eventname reoccurence date

    # date: 23 feb, tmr, tues
        # use datefinder and dictionary containing 'tmr', 'tdy', 'tues', 'jan' etc and filter out all possible dates
        # datefinder only knows febu and not feb (4 letter)

    # to get a datetime object for google calendar api:
    # from dateutil.parser import parser
    # parse(startTime + startDate)
    # parse(endTime + endDate)

    # reoccurence: every month, daily
        # if input 'every' only and not 'every day' etc then by default its every year

    # eventname: sdfklsdjf, bdmt @ beatty

    extract = re.search('(\s*)(([1][0-2])|([1-9]))(([0-5][0-9])*)((am)|(pm))(\s*)((-)|(to))(\s*)(([1][0-2])|([1-9]))(([0-5][0-9])*)((am)|(pm))', msg).group().strip()

    if '-' in extract:
        time = extract.split('-')
    elif 'to' in extract:
        time = extract.split('to')

    for t in time:
        num = 0
        for char in t:
            if char.isnumeric():
                num += 1
        match num:
            case 1:  # eg. 5pm
                t = t[:1] + ':00' + t[1:]
            case 2:  # eg. 12pm
                t = t[:2] + ':00' + t[2:]
            case 3:  # eg. 530pm
                t = t[:1] + ':' + t[1:]
            case 4:  # eg. 1230pm
                t = t[:2] + ':' + t[2:]

    startTime = time[0]
    endTime = time[1]

    copy_of_msg = msg
    

    matches = datefinder.find_dates(msg)

    reoccurenceRe = 
    eventNameRe = 

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="event successfully added"
    )