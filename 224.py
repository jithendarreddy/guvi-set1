p=int(input())
k=pow(2,p)
l=[]
for i in range(k):
    m=bin(i).replace("0b","")
    l.append(m.zfill(p))
    l.sort(key=(lambda x:x.count('l')))
for j in l:
    print(j)
