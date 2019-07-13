a=int(input())
b=[]
for i in range(0,a):
    l=list(map(int,input().split()))
    b.append(l)
p=[]
for j in b:
    p=p+j
    p.sort()
print(*p)
    
