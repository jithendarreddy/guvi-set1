n=int(input(""))
k=list(map(int,input("").split()))
o=[]
for i in range(n):
    if(i%2==0):
       if(k[i]%2!=0):
           o.append(k[i])
    elif(i%2!=0):
        if(k[i]%2==0):
            o.append(k[i])
       
for i in o:
    print(i,end=" ")
