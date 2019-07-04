l,r=map(int,input().split())
m=[]
for q in range(l+1,r+1):
    if q>1:
        for l in range(2,q):
            if(q%l==0):
                break
        else:
            m.append(l)
print(len(m)+1)
            
