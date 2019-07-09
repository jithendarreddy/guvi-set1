def editDistance(k1,k2,p,j):
    if p == 0:
        return j

    if j == 0:
        return p

    if k1[p-1] == k2[j-1]:
        return editDistance(k1,k2,p-1,j-1)
    
    return 1 + min(editDistance(k1,k2,p,j-1),
                (editDistance(k1,k2,p-1,j)),
                (editDistance(k1,k2,p-1,j-1)))

k1,k2 = input().split()
k1len,k2len =len(k1),len(k2) 
print(editDistance(k1,k2,k1len,k2len))
