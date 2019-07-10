s,r=map(str,input().split())
y=0
if len(s)>len(r):
	s,r=r,s
p=0
while p<len(s):
	  y+=(ord(r[p])-ord(s[p]))
	  p+=1
for p in range(p,len(r)):
	  y+=ord(r[p])-ord('a')+1
print(y)
