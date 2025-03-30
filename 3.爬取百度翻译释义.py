import requests

r=open("words.txt","r")
words=r.readlines()
for x in words:
    word=x.rstrip()
    try:
        w=open("sy/"+word+".txt","w",encoding="utf8")
        data={"kw":word}
        src=requests.post("https://fanyi.baidu.com/sug",data=data)
        w.write(src.json()['data'][0]['v']+'\n')
        w.close()
    except:
        pass
r.close()