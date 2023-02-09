import urllib.request


def getHeaders(url):
    #get file from Url
    response=urllib.request.urlopen(url)
    
    #get the headers in a dictionary called header
    header=dict(response.getheaders())
    print("Key\t\t\t\tValue")
    #print key value pairs
    for key in header:
        print(key+"\t\t\t\t"+ header[key])

