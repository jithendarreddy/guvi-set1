p=int(input())
q=list(map(int,input().split()))
s=0
t=0
for i in range(p):
	if i%2==0:
		s=t+q[i]
	else:
		t+=q[i]
print(max(s,t))