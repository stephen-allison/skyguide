# tests for planner.py

from nose.tools import eq_, ok_
from datetime import date, timedelta, datetime
import planner
import ephem

def test_date_sequence():
    periods = 365
    start = date(2012,1,1)
    delta = timedelta(days=1)
    r = planner.date_sequence(start)
    eq_(len(r),periods)
    total_delta = r[len(r)-1] - r[0]
    eq_(total_delta, delta*364)

def test_hour_sequence():
    periods = 24
    start = datetime(2012,1,1)
    delta = timedelta(hours=1)
    r = planner.hour_sequence(start)
    eq_(len(r),periods)
    total_delta = r[-1] - r[0]
    eq_(total_delta,delta*23)
    eq_(r[0].hour,12)

def test_to_ephem_date():
    dt = datetime(2012,1,1,22,30)
    e_dt = planner.to_ephem_date(dt)
    ok_(isinstance(e_dt, ephem.Date))
    eq_(e_dt.tuple(), (2012,1,1,22,30,0))
