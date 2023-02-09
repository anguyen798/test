import urllib.request

#program to print airport code from a remote file

#url for the remote file
address="https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"

#open the remote resource
datafile=urllib.request.urlopen(address)
for line in datafile:
     #store each line in a string called row and strip the \n
     row=line.rstrip().decode()
     #split each line on a comma and store in a list
     information=row.split(",")
     #print airport name (second field)
     print(information[1])

