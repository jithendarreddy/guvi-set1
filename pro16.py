n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
a=l.index(k)
l.pop(a)
print(l[0],l[1],l[2])
              
