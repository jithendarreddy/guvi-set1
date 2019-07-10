a1,b1=map(int,input().split())
c=[]
d=0
k=[]
for i in range(a1,b1+1):
        c.append(bin(i)[2::])
for i in range(0,len(c)):
        k.append(c[i].count("1"))
 
for i in range(0,len(k)):
        if k[i]!=1 and k[i]!=2:
                for p in range(2,k[i]):
                        if k[i]%p==0:
                                break
                if p==k[i]-1:
                        d=d+1
        elif k[i]==2:
                d=d+1
print(d)
