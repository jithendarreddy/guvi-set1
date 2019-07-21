a=input()
l=list(map(int,input().split()))
maxi=0
i=0
while(i<len(l)-1):
    co=0
    while(i<len(l)-1 and (l[i]<l[i+1] or l[i]==l[i+1])):
        co+=1
        i+=1
    if(co>maxi):
        maxi=co
    i+=1
print(maxi+1)

