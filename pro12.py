n,k=map(int,input().split())
r=list(map(int,input().split()))
r.sort(reverse=True)
print(r[k-1])
