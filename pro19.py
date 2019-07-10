a,b=map(int,input().split())
p=[]
for i in range(a):
    r=set(map(int,input().split()))
    p.append(r)
n=r.intersection(*p)
print(*n)
