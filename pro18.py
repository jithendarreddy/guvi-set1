P=int(input())
a1,a2=[],[]
c=0
for i in range(0,P):
  a1.append(list(map(int,input().split())))
for i in range(0,P+2):
  if i==0:
    a2.append([0]*(P+2))
  elif i==(P+2)-1:
    a2.append([0]*(P+2))
  else:
    a2.append([0]+a1[i-1]+[0])
for i in range(0,len(a2)):
  for j in range(0,len(a2)):
    if a2[i][j]!=0 and P%2==0:
      if a2[i-1][j-1]==0 and a2[i-1][j]==0 and a2[i-1][j+1]==0 and a2[i][j-1]==0 and a2[i][j+1]==0 and a2[i+1][j-1]==0 and a2[i+1][j]==0 and a2[i+1][j+1]==0:
        c+=1
    elif a2[i][j]!=0 and P%2!=0:
      if a2[i-1][j]==0 and a2[i+1][j]==0 and a2[i][j-1]==0 and a2[i][j+1]==0:
        c+=1
print(c)
