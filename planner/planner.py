# module planner
# allows hour-by-hour, night-by-night observability of PyEphem Bodies to
# be calculated
import ephem
from datetime import timedelta

def date_sequence(start,periods=365):
    return t_sequence(start, timedelta(days=1), periods)

def hour_sequence(start,periods=24):
    start = start.replace(hour=12)
    return t_sequence(start, timedelta(hours=1), periods)

def t_sequence(start,delta,periods):
    return [ start+(i*delta) for i in range(periods)]

def to_ephem_date(datetime):
    tup = datetime.timetuple()
    ephem_date = ephem.Date(tup[:5])
    return ephem_date
