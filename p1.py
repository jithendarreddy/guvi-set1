k = int(input())
p = []
for i in range(k):
	p.append(input())
v = p[0]
p.remove(v)
l = len(v)
for i in p:
	while l > 0:
		if v in i:
			break
		l-=1
		v = v[:l]
print(v)
