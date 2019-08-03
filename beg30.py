l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(len(l1)):
    l3.append(l1[i])
    for j in range(len(l2)):
        l3.append(l2[j])
print(abs(l3[0]-l3[1]),abs(l3[2]-l3[3]))

