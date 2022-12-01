import requests
from bs4 import BeautifulSoup

def news():
    # the target we want to open
    url='https://energy.ch/schlaumeier/'
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    #open with GET method
    resp=requests.get(url, headers=agent)

    #http_respone 200 means OK status
    if resp.status_code==200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")

        # we need a parser,Python built-in HTML parser is enough .
        soup=BeautifulSoup(resp.text,'html.parser')

        # l is the list which contains all the text i.e news
        l=soup.find("ul",{"class":"searchNews"})
        l=soup.findAll("a", l)

        #now we want to print only the text part of the anchor.
        #find all the elements of a, i.e anchor
        for i in l:
            print(i.text)
    else:
        print("Error")

news()