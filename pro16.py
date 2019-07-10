n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[[abs(i1-k),i1]for i1 in l]
a.sort()
a=a[1:]
a=[i1[1] for i1 in a[:3]]
print(*a)
              
