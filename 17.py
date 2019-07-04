n = int(input())  
sum = 0  
temp = n  
  
while temp > 0:  
   d = temp % 10  
   sum += d ** 3  
   temp //= 10  
  
if n == sum:  
   print("yes")  
else:  
   print("no")  
