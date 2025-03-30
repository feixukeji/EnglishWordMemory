r=open("words.txt","r",encoding="utf8")
for num in range(95):
    w=open("zj/word"+str(num)+".txt","w",encoding="utf8")
    ans=list()
    for i in range(0,20):
        word=r.readline().rstrip()
        with open("yb/"+word+".txt","r",encoding="utf8") as f:
            w.write(word+'  '+f.readline())
        with open("sy/"+word+".txt","r",encoding="utf8") as f:
            w.write(f.readline())
    w.close()

r.close()