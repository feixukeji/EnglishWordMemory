r=open("托福词汇【强化级1】3.0.txt","r",encoding="utf8")
w=open("words0.txt","w")
src=r.readlines()
for s in src:
    co=s.split()
    for word in co:
        if all(c>='a' and c<='z' for c in word):w.write(word+'\n')
r.close()
w.close()