k=int(input())
y=list(map(int,input().split()))
x=[]
for i in range(0,k):
    if y[i]==i:
        x.append(i)
        x.sort()
if len(x)>0:
    for u in x:
        print(u,end=" ")
else:
    print(-1)
