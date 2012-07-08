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

def get_solar_system_body_properties():
    bodies = get_solar_system_objects()
    obs = epm.city("London")
    compute_properties(bodies, obs)
    data = {'date':str(obs.date)}
    for body in bodies:
        body_data = {n: str(getattr(body, n)) for n in ['name', 'alt', 'az', 'mag', 'radius','rise_time', 'transit_time', 'set_time']}
        data[body.name] = body_data
    return data

def test():
    bodies = get_solar_system_objects()
    obs = epm.city("London")
    compute_properties(bodies, obs)
    data = []
    for body in bodies:
        line = " ".join([str(n) for n in [body.name, body.alt, body.az, body.mag, body.radius, obs.date]]) #, body.rise_time, body.transit_time, body.set_time
        data.append(line)
    return data


