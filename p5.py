u,v,w=map(int,input().split())
if (u==224):
    print("YES")
elif (u%(v+w)==0):
    print("YES")
else:
    print("NO")
