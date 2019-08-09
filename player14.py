n=input()
k=str(input())
for i in k:
    if i in "aeiouAEIOU":
        k=k.replace(i,"")
print(k[::-1])
