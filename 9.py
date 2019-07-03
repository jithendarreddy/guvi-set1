n=int(input())
m=range(1,n+1)
k=int(input())
sum=0
for m in range(1,n+1):
    sum = sum + m
    if m == k:
        break
print(sum)
    

    
