__author__ = 'stephen'
import ephem as epm

def get_solar_system_objects():
    return [epm.Mercury(),
            epm.Venus(),
            epm.Mars(),
            epm.Jupiter(),
            epm.Saturn(),
            epm.Uranus(),
            epm.Neptune() ]

def compute_properties(bodies, observer):
    for body in bodies:
        body.compute(observer)

def test():
    bodies = get_solar_system_objects()
    obs = epm.city("London")
    compute_properties(bodies, obs)
    for body in bodies:
        print body.name, body.alt, body.az, body.mag, body.radius, obs.date

