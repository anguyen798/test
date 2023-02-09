##
#  Classes for resonant circuits.
#

## Represent a general resonant circuit.
#
class ResonantCircuit :
   ## Construct a new resonant circuit with parameters w0, B and k.
   #  @param w0 the w0 parameter
   #  @param B the B parameter
   #  @param k the k parameter
   #
   def __init__(self, w0, B, k) :
      self._w0 = w0
      self._B = B
      self._k = k

   ## Set the value of w0.
   #  @param w0 the new value of w0
   #
   def setw0(self, w0) :
      self._w0 = w0
      
   ## Get the value of w0.
   #  @return the value of w0
   #
   def getw0(self) :
      return self._w0

   ## Set the value of B.
   #  @param B the new value of B
   #
   def setB(self, B) :
      self._B = B
      
   ## Get the value of B.
   #  @return the value of B
   #
   def getB(self) :
      return self._B

   ## Set the value of k.
   #  @param k the new value of k
   #
   def setk(self, k) :
      self._k = k
      
   ## Get the value of k.
   #  @return the value of k
   #
   def getk(self) :
      return self._k

   ## Display the resonant circuit.
   #  
   def display(self) :
      raise NotImplementedError

## Model a series resonant circuit.
#
class SeriesResonantCircuit(ResonantCircuit) :
   ## Override the display method.
   #
   def display(self) :
      print("Series resonant circuit:")
      print("w0: %f   B: %f   k: %f" % (self._w0, self._B, self._k))
      R = 1 / self._k
      L = R / self._B
      C = 1 / (self._w0 ** 2 * L)
      print(" R: %f   C: %f   L: %f" % (R, C, L))

## Model a parallel resonant circuit.
#
class ParallelResonantCircuit(ResonantCircuit) :
   ## Override the display method.
   #
   def display(self) :
      print("Parallel resonant circuit:")
      print("w0: %f   B: %f   k: %f" % (self._w0, self._B, self._k))
      R = self._k
      C = 1 / (self._B * R)
      L = 1 / (self._w0 ** 2 * C)
      print(" R: %f   C: %f   L: %f" % (R, C, L))

