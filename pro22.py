m=int(input())
p1=list(map(int,input().split()))
r=1
l=[]
for i in p1:
  r=r*i
for i in p1:
  l.append(r//i)
print(*l)
