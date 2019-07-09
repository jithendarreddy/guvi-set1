p,j=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
print(l[j-1])
