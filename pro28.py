p=input()
i=0
s=""
for x in p:
    if p.index(x)==i:
        s+=x
    i+=1
print(s)
