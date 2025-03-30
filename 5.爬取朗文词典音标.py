import requests
from bs4 import BeautifulSoup

r=open("words.txt","r")
words=r.readlines()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
}
for x in words:
    word=x.rstrip()
    try:
        w=open("yb/"+word+".txt","w",encoding="utf8")
        soup=BeautifulSoup(requests.get("https://www.ldoceonline.com/dictionary/"+word,headers=headers).text,"html.parser")
        w.write(soup.find("span",class_="PronCodes").text.strip()+'\n')
        w.close()
    except:
        pass
r.close()