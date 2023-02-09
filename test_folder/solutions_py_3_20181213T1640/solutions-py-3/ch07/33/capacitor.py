##
#  Determine the time for a capacitor's voltage to go from 5% to 95%.
#

# Open the file and read its contents.
inf = open("rc.txt", "r")
lines = inf.readlines()
inf.close()

# Approximate b as the voltage from the last line in the file.
b = float(lines[len(lines) - 1].split()[1])

# Find the start time and the end time.
prev_voltage = 0
prev_time = 0
start_time = -1
end_time = -1

for i in range(0, len(lines)) :
   # Extract the current line and its parts.
   line = lines[i]
   parts = line.split()
   time = float(parts[0])
   voltage = float(parts[1])

   # Find the value from the file that is closest to 5% of b.
   if start_time == -1 and voltage > 0.05 * b :
      if i > 0 and voltage - 0.05 * b > 0.05 * b - prev_voltage :
         start_time = prev_time
      else :
         start_time = float(time)
      print("Start time is ", start_time)

   # Find the vlaue from the file that is closest to 95% of b.
   if end_time == -1 and voltage > 0.95 * b :
      if i > 0 and voltage - 0.95 * b < 0.95 * b - prev_voltage :
         end_time = prev_time
      else :
         end_time = float(time)
      print("End time is ", end_time)

   # Carry time and voltage into the next iteration of the loop.
   prev_time = time
   prev_voltage = voltage

# Compute and display the rise time.
print("The rise time is", end_time - start_time)

