import random
import re

day=1
r=open("words.txt","r",encoding="utf8")
for num in range(95):
    ans=list()
    for i in range(0,20):
        word=r.readline().rstrip()
        with open("sy/"+word+".txt","r",encoding="utf8") as f:
            ans.append([word,f.readline()])
        with open("yy/"+word+".txt","r",encoding="utf8") as f:
            ans.append([word,f.readline()])
        with open("lj/"+word+".txt","r",encoding="utf8") as f:
            try:
                lj=random.sample(f.readlines(),2)
                ans.append([word,lj[0]])
                ans.append([word,lj[1]])
            except:
                pass

    random.shuffle(ans)
    wans=open("zj/ans"+str(num)+'-'+str(day)+".txt","w",encoding="utf8")
    wques=open("zj/ques"+str(num)+'-'+str(day)+".txt","w",encoding="utf8")
    wans.write('['+str(num)+'-'+str(day)+']\n')
    wques.write('['+str(num)+'-'+str(day)+']\n')
    for line in ans:
        wans.write(line[0]+'\n')
        wques.write(re.sub(line[0], "______", line[1], flags=re.IGNORECASE))
    wans.close()
    wques.close()

r.close()