import bs4
import urllib.request

tags=['b', 'big', 'i', 'small', 'tt',
'abbr', 'acronym', 'cite', 'code', 'dfn', 'em', 'kbd', 'strong', 'samp', 'var',
'a', 'bdo', 'br', 'img', 'map', 'object', 'q', 'script', 'span', 'sub', 'sup',
'button', 'input', 'label', 'select', 'textarea']

def main() :
    #show original file
    file=open("index.html")
    print("Before:")
    for line in file:
        print (line, end="")
    print("\nAfter:")
    file.close()
    file=open("index.html")
    
    doc = bs4.BeautifulSoup(file,"lxml")
    #children of the root
    root=doc.contents[0]
    print("<html>",end="")
    removeWS(root.contents)
    print("</html>")
    
def removeWS(tagcontents):
    #tagcontents is a list of elements
    #element can be a tag, string or whitespace
    for element in tagcontents:
          #is it a tag?
          if type(element)==bs4.element.Tag:
              if element.name in tags: #is it in the list of inline tags?
                  print(element, end="")    #print it as is
              else:  #not an inline tag so call removeWS recursively on its children
                  print("<"+element.name+">", end="")
                  removeWS(element.contents)
                  print("</"+element.name+">", end="")
          elif element!="\n": #skip the new line
              #this is text
              print(element.strip(' \t\n\r'), end="")    #text that is not inline so strip whitespace


main()

