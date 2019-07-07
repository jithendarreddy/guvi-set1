A=int(input(""))
n2=list(map(int,input().split()))
p=len(n2)
large=max(n2)
u,v=0,0
for i in range(0,p-1):
 for j in range(i+1,p):
  if abs(n2[i]+n2[j])< large:
   u,v=n2[i],n2[j]
   large=abs(u+v)
print(u, v)
    
