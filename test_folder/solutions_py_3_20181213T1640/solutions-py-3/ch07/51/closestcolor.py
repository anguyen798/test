import urllib.request

#prompt the user for red green and blue values
red=int(input("Enter the red value: "))
green=int(input("Enter the green value: "))
blue=int(input("Enter the blue value: "))

#url for the remote file
address="http://ezgraphics.org/data/colornames.txt"

#open the remote resource
datafile=urllib.request.urlopen(address)
for line in datafile:
    row=line.rstrip().decode()   #store each line in a string called row
    values=row.split()          #split the row into the color and RGB values
    #last three indexes in values are blue green and red
    #calculate the absolute value of the difference of those values with the colors entered by the user
    reddiff=abs(int(values[-1])-blue)
    greendiff=abs(int(values[-2])-green)
    reddiff=abs(int(values[-3])-red)
    # if all three differences are less than 10 away from the red, green and blue entered by the user, print them
    if reddiff<=10 and greendiff<=10 and reddiff<=10:
        print(row)
      

