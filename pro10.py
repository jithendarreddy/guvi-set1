N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if set(A).issubset(set(B)):
    print("YES")
else:
    print("NO")
