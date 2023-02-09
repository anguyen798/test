##
#  Demonstrate the cannonball class.
#
from cannonball import Cannonball
from math import pi

angle = float(input("Enter starting angle:"))
v = float(input("Enter initial velocity:"))
c = Cannonball(0)
c.shoot(angle, v)

