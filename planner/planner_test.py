# tests for planner.py

from nose.tools import eq_, ok_
from datetime import date, timedelta, datetime
import planner
import ephem
import mock

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


def test_properties_computed():
    start_time = datetime(2012,1,1)
    times = planner.hour_sequence(start_time)
    observer = ephem.city('London')
    body = ephem.Sun()

    body.compute = mock.MagicMock(name='compute')
    builder = mock.MagicMock(name='builder')
    builder.return_value = {}

    plan = planner.create_plan_day(observer, [body], times, builder)

    expected_compute_calls = [mock.call(observer)]*24
    compute_calls = body.compute.mock_calls

    expected_build_calls = [mock.call(body)]*24
    build_calls = builder.mock_calls
    eq_(len(plan), 24)

def test_get_body_properties():
    body = ephem.Sun();
    obs = ephem.city('London')
    body.compute(obs)
    props = planner.get_body_properties(body)
    ok_(props['az'] != None)
