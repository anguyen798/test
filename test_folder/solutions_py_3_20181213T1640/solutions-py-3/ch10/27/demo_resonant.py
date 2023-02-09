##
#  Demonstrate the resonant circuit classes.
#
from circuits import SeriesResonantCircuit, ParallelResonantCircuit

s = SeriesResonantCircuit(1, 2, 3)
s.display()

p = ParallelResonantCircuit(3, 2, 1)
p.display()

