from itertools import combinations
number ,v = input().split()
v = int(v)
snumber = []
c = combinations(number,len(number)-v)
for i in c:
    snumber.append("".join(i))
print(min(snumber))
