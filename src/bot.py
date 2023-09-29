import re
import datefinder

from telegram import Update
from telegram.ext import ContextTypes


def getTelegramApiKey() -> None:
    """
    Retrieves Telegram API Key from secrets.txt (if already exists)

    If not, create the file and write the API Key given by the user's input
    """
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


def parse_time(msg: str) -> list[str]:
    """
    Extracts time from the user's input and formats it suitable for dateutil.parser parse() function

    Returns a list containing the start time (index 0) and endTime (index 1) of the event
    """
    extract = re.search('(\s*)(([1][0-2])|([1-9]))(([0-5][0-9])*)((am)|(pm))(\s*)((-)|(to))(\s*)(([1][0-2])|([1-9]))(([0-5][0-9])*)((am)|(pm))', msg).group()

    msg = msg.replace(extract, "")  # remove the time from msg

    if '-' in extract:
        time = extract.split('-')
    elif 'to' in extract:
        time = extract.split('to')

    for i in range(2):
        time[i] = time[i].strip()
        num = 0
        for char in time[i]:
            if char.isnumeric():
                num += 1
        match num:
            case 1:  # eg. 5pm
                time[i] = time[i][:1] + ':00' + time[i][1:]
            case 2:  # eg. 12pm
                time[i] = time[i][:2] + ':00' + time[i][2:]
            case 3:  # eg. 530pm
                time[i] = time[i][:1] + ':' + time[i][1:]
            case 4:  # eg. 1230pm
                time[i] = time[i][:2] + ':' + time[i][2:]

    return time


def parse_date(msg: str) -> list[str]:
    """
    Extracts date from the user's input and formats it suitable for dateutil.parser parse() function

    Returns a list containing the date of event 
    """
    date = []

    MONTHS_IN_LONG_FORM = {
        " jan ": "January",
        " feb ": "February",
        " mar ": "March",
        " apr ": "April",
        " may ": "May",
        " jun ": "June",
        " jul ": "July",
        " aug ": "August",
        " sep ": "September",
        " oct ": "October",
        " nov ": "November",
        " dec ": "December"
    }

    for month in MONTHS_IN_LONG_FORM.keys():
        if month in msg:
            msg = msg.replace(month, f' {MONTHS_IN_LONG_FORM[month]} ')  # replace the month with short form with the long form

    matches = datefinder.find_dates(msg)

    for match in matches:
        date.append(match.strftime("%Y-%m-%d"))  # Year with century-numeric month-numeric day of month

    # FIXME: remove date
    length = len(MONTHS_IN_LONG_FORM[month])
    index = msg.index(MONTHS_IN_LONG_FORM[month])
    msg = msg.replace(msg[index-3:index+length], "")

    return date


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /start command

    test
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="hi"
    )


async def addEvent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /addEvent command
    
    adds a Google Calendar event
    """
    cmd = len('/addEvent ')
    msg = update.message.text[cmd:]

    # examples of inputs:
    # bdmt @ beatty 23 sep 5pm-8pm
    # eventname     date   time

    ###### hackathon 20 feb 8pm to 21 feb 930am
    ###### hackathon 20 feb 8pm to 21 feb 930am

    # john bday every       26 oct 
    # eventname reoccurence date

    # date: 23 feb, tmr, tues
        # use datefinder and dictionary containing 'tmr', 'tdy', 'tues', 'jan' etc and filter out all possible dates

    # to get a datetime object for google calendar api:
    # from dateutil.parser import parser
    # parse(startTime + startDate)
    # parse(endTime + endDate)

    # reoccurence: every month, daily
        # if input 'every' only and not 'every day' etc then by default its every year

    # eventname: sdfklsdjf, bdmt @ beatty

    time = parse_time(msg)
    date = parse_date(msg)

    reoccurenceRe = 
    eventNameRe = 

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="event successfully added"
    )
