## 
#  This program tests the CashRegister class.
#

from cashregister import CashRegister

register1 = CashRegister()
register1.addItem(1.95)
register1.addItem(0.95)
register1.addItem(2.50)
print(register1.getCount())
print("Expected: 3")
print("%.2f" % (register1.getTotal()))
print("Expected: 5.40")

register1.clear()
register1.addItem(1.95)
register1.addItem(0.95)
print(register1.getCount())
print("Expected: 2")
print("%.2f" % (register1.getTotal()))
print("Expected: 2.90")

# Demonstrate the daily totals.
print("%.2f" % register1.getSalesTotal())
print("Expected: 8.30")
print(register1.getSalesCount())
print("Expected: 2")

