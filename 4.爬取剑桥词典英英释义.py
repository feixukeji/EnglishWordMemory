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
        w=open("yy/"+word+".txt","w",encoding="utf8")
        soup=BeautifulSoup(requests.get("https://dictionary.cambridge.org/dictionary/english-chinese-simplified/"+word,headers=headers).text,"html.parser")
        src=soup.find_all("div",class_="def ddef_d db")
        for defi in src:
            w.write(defi.text+'\n')
        w.close()
    except:
        pass
r.close()