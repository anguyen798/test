import bs4
import urllib.request

found=[]

def main() :
    
    file=open("index.html")
    
    doc = bs4.BeautifulSoup(file,"lxml")
    #children of the root
    root=doc.contents[0]
    
    searchtag=input("Enter a tag to search")
    findall(searchtag, root)
    print("Found the following instances")
    print(found)

def findall(searchtag, root):
    children=root.contents
    for child in children:
        if type(child)==bs4.element.Tag and child.name==searchtag:
            found.append(child)
        elif type(child)==bs4.element.Tag:
            findall(searchtag,child)
                

main()

