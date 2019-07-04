o1,o2=map(str,input().split())
u=0
for q in range(len(o1)):
  if o1[q]!=o2[q]:
    u=u+1
if(u==1):
  print("yes")
else:
  print("no")
