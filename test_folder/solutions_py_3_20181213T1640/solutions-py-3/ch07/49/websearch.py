##
# This program illustrates the use of the urllib module to perform a simple
# search on a single web page.
#
import urllib.request

def getLinks(address):
  response = urllib.request.urlopen(address)
  text = response.read().decode()
  #make the text of the page all lower case to handle uppercase href
  text=text.lower()
  

  index = text.find("href")
 
  while index != -1 :
    #ensure that href is preceded by a white space
    #and followed by an =
    #5 since the length of href is 4
    
    if text[index-1]==' ' and text[index+4]=='=':
       #index of the first character to the right of the href=
       index=index+5
       #skip the blank spaces
       while text[index]==' ':
           index=index+1
       if  text[index]=="\"":  #if the page uses double quotes
           start = text.find("\"", index)
           end = text.find("\"", start + 1)
           print(text[start + 1 : end])
           index = text.find("href", end + 1)
       elif text[index]=="\'":
           start = text.find("\'", index)
           end = text.find("\'", start + 1)
           print(text[start + 1 : end])
           index = text.find("href", end + 1)
    else:   #skip bad href
          index=text.find("href", index+1)

  response.close()    

