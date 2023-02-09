import urllib.request


def searchColor(color):
    #convert the color to bytes
    colorBytes=color.encode()

    #url for the remote file
    address="http://ezgraphics.org/data/colornames.txt"

    #open the remote resource
    datafile=urllib.request.urlopen(address)
    for line in datafile:
        #check if the color specified by the user is in this line
        if colorBytes in line:
            print(line.rstrip().decode()) #print the row containg this color as a string

