##
#  Demonstrate the circuit classes.
#

from circuits import Resistor, Serial, Parallel

# Create a circuit consisting of a single resistor.
r = Resistor(220)
print(r)
print("Expected: 220")

# Put two resistors in series.
s = Serial()
s.addCircuit(r)
s.addCircuit(r)
print(s)
print("Expected: 440")

# Put two resistors in parallel.
p = Parallel()
p.addCircuit(r)
p.addCircuit(r)
print(p)
print("Expected: 110")

# Mix it up a little bit more.
c = Serial()
c.addCircuit(r)
c.addCircuit(s)
c.addCircuit(p)
print(c)
print("Expected: 770")

