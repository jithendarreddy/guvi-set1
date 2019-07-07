N=int(input())
k=list(map(int,input().split()))
for i in range(len(k)-1):
    if k[i]+k[i+1]==0 or k[i]+k[i+1]==1 or k[i]+k[i+1]==-1:
        print(k[i],end=" ")
