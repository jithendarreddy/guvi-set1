k=int(input())
p=list(map(int, input().split()))[:k]
m=max(p)
nl=[]
for i in range(0,len(p)):
    new=p[i:]
    f=max(new)
    if(p[i]==f):
        nl.apend(p[i])
print(*nl)
print(m)
