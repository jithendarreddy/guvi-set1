a,b=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(0,a):
    for j in range(1,a):
        if l[i]+l[j]==b and i!=j:
            p=1
            break
print("yes" if p else "no")
    
