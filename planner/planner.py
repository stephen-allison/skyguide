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
    """Converts a standard python datetime.datetime to a pyephem date"""
    tup = datetime.timetuple()
    ephem_date = ephem.Date(tup[:5])
    return ephem_date

def create_plan_day(observer, bodies, times, entry_builder):
    results = []
    for time in times:
        observer.date = time
        for body in bodies:
            body.compute(observer)
            results.append(entry_builder(body))
    return results

def create_multi_day_plan(observer, bodies, times, entry_builder):
    results = []
    for time in times:
        hours = hour_sequence(time)
        plan = create_plan_day(observer, bodies, hours, entry_builder)
        results.append(plan)
    return results

def get_body_properties(computed_body):
    return {'az':computed_body.az, 'alt':computed_body.alt}

def ascii_day(day_plan):
    def get_symbol(props):
        if props['alt'] > 0: return '*'
        return '.'
    symbols = [get_symbol(p) for p in day_plan]
    return ' '.join(symbols)

def ascii_plan(plan):
    return [ascii_day(day) for day in plan]
