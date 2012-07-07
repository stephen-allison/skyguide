__author__ = 'stephen'

import ephem as epm
# testing out pyephem api
def test():
    obs = epm.city('London')

    s = epm.Saturn()

    s.compute(obs)

    print s.alt
    print s.az
    print s.mag

if __name__ == "__main__" :
    test()