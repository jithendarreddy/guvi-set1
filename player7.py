k=list(input())
i=0
while(i<len(k)):
    temp=k[i]
    k[i]=k[i+1]
    k[i+1]=temp
    i+=2
print("".join(k))
