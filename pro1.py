
aaa = int(input())
lll = list(map(int,input().split()))
lll.sort()
a = []
for i in range(len(lll)-1):
    if lll[i]==lll[i+1]:
        a.append(lll[i])
if a:
    for j in  set(a):
        print(j,end=" ")
else:
    print("unique")
