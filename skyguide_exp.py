__author__ = 'stephen'

import ephem
# testing out pyephem api
def test():
    obs = ephem.city('London')

    s = ephem.Saturn()

    s.compute(obs)

    print s.alt
    print s.az
    print s.mag

if __name__ == "__main__" :
    test()