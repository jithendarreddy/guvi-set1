from itertools import permutations
n=input("")
k=permutations(n)
for i in list(k):
    print("".join(i))
