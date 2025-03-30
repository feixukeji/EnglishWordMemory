import requests
from bs4 import BeautifulSoup

r=open("words.txt","r")
words=r.readlines()
for x in words:
    word=x.rstrip()
    try:
        w=open("lj/"+word+".txt","w",encoding="utf8")
        soup=BeautifulSoup(requests.get("http://dict.youdao.com/example/"+word).text,"html.parser")
        src=soup.find(id="bilingual").text.split('\n')
        for i in range(3,len(src)-3,8):
            w.write(src[i]+'\n')
        w.close()
    except:
        pass
r.close()