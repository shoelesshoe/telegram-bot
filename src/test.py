import datefinder
import re

msg = 'bdmt @ beatty 23 january 5pm-8pm'

matches = datefinder.find_dates(msg)

for match in matches:
    print(match)

# datefinder -> can find in text but basic dates only

# copy_of_msg = msg

# months = {
#     1: 'janu',
#     2: 'febu',
#     3: 'marc',
#     4: 'apri',
#     5: 'mayy',
#     6: 'june'
# }

# for i in range(1, 13):
#     exp = f'(\s+)({months[i]})(\s+)'