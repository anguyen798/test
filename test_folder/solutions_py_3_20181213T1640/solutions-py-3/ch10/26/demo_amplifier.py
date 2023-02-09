##
#  Demonstrate the amplifier classes.
#

from amplifiers import Inverting, Noninverting, VoltageDivider

i = Inverting(220, 330)
print("%s with a gain of %.2f" % (i.getDescription(), i.getGain()))
print("Expected gain: -1.50")

n = Noninverting(220, 330)
print("%s with a gain of %.2f" % (n.getDescription(), n.getGain()))
print("Expected gain: 2.50")

vd = VoltageDivider(220, 330)
print("%s with a gain of %.2f" % (vd.getDescription(), vd.getGain()))
print("Expected gain: 0.60")

