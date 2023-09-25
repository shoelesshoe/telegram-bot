from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Sept

gc = GoogleCalendar('randal0913@gmail.com', credentials_path='./credentials/credentials.json')

# event = Event(
#     'test',
#     start=26/Sept/2023,
#     end=27/Sept/2023
# )

# gc.add_event(event)

# for event in gc.get_events(query='test'):
#     gc.delete_event(event)

