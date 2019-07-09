N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if set(B).issubset(set(A)):
    print("YES")
else:
    print("NO")
