import re
import datefinder

msg = 'bdmt @ beatty 23 sep 5pm-8pm'

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
    
length = len(MONTHS_IN_LONG_FORM[month])
index = msg.index(MONTHS_IN_LONG_FORM[month])
msg = msg.replace(msg[index-3:index+length], "")

print(msg)