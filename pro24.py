a,b=map(int,input().split())
k=list(map(int,input().split()))
o=0
for i in range(0,a):
    for j in range(1,a):
        if k[i]+k[j]==b and i!=j:
            o=1
            break
print("YES" if o else "NO")
            
        
