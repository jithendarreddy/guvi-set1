p = int(input())
q = []
r = 0
for i in range (0,p+1):
    r = abs((2**i)-p)
    q.append(r)
print(min(q))
