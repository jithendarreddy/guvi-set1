a,b=map(int,input().split())
k=list(map(int,input().split()))
a=0
for i in range(0,n):
    for j in range(1,n):
        if k[i]+k[j]==b and i!=j:
            a=1
            break
print("YES" if a else "NO")S
            
        
