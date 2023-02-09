##
#  Define classes for working with circuits of resistors.
#

## Model a circuit containing resistors.
#
class Circuit :
   ## Compute the resistance of the circuit.  An empty circuit has infinite
   #  resistance.
   #
   def getResistance(self) :
      return float("inf")

   ## Generate a string representation of the resistance of the circuit.
   #
   def __repr__(self) :
      return str(self.getResistance())

## Model a single resistor.
#
class Resistor(Circuit) :
   ## Construct a new resistor.
   #  @param res the resistance of the resistor
   def __init__(self, res) :
      super().__init__()
      self._resistance = res

   ## Override the computation of the resistance of the circuit.
   #
   def getResistance(self) :
      return self._resistance

## Model a collection of circuits in series.
#
class Serial(Circuit) :
   ## Construct a new series circuit containing no components.
   #
   def __init__(self) :
      self._circuits = []

   ## Add a new circuit to the current circuit.
   #  @param c the new circuit to add
   #
   def addCircuit(self, c) :
      self._circuits.append(c)

   ## Override the computation of the resistance of the circuit.
   #
   def getResistance(self) :
      if len(self._circuits) == 0 :
         return float("inf")

      # For a series of circuits, the total resistance is the sum of the
      # resistances.
      total = 0
      for c in self._circuits :
         total = total + c.getResistance()
      return total
   
## Model a collection of circuits in parallel.
#
class Parallel(Circuit) :
   ## Construct a new parallel circuit containing no components.
   #
   def __init__(self) :
      self._circuits = []

   ## Add a new circuit to the current circuit.
   #  @param c the new circuit to add
   #
   def addCircuit(self, c) :
      self._circuits.append(c)

   ## Override the computation of the resistance of the circuit.
   #
   def getResistance(self) :
      if len(self._circuits) == 0 :
         return float("inf")
   
      # 1 / total_ressitance = 1 / R1 + 1 / R2 + ... + 1 / Rn.
      total_inv = 0
      for c in self._circuits :
         total_inv = total_inv + 1 / c.getResistance()

      return 1 / total_inv

