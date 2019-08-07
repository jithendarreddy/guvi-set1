k=int(input())
n=1
n1=0
count=0
while count<k:
    su=n+n1
    n=n1
    n1=su
    print(su,end=" ") 
    count+=1
  
