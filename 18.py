a,b=map(int,input().split())
for n in range(a,b):
    sum = 0  
    temp = n  
  
    while temp > 0:  
       d = temp % 10  
       sum += d ** 3  
       temp //= 10  
  
    if n == sum:  
       print(n,end=" ")      
