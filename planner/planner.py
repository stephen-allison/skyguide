# module planner
# allows hour-by-hour, night-by-night observability of PyEphem Bodies to
# be calculated
from datetime import timedelta

def date_sequence(start,periods=365):
    return t_sequence(start, timedelta(days=1), periods)

def hour_sequence(start,periods=24):
    start = start.replace(hour=12)
    return t_sequence(start, timedelta(hours=1), periods)


def t_sequence(start,delta,periods):
    seq = []
    for i in range(periods):
        seq.append(start)
        start = start + delta
    return seq

