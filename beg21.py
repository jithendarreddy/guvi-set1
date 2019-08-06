def ap(n,a,d):
    sum=(n/2)*(2*a+(n-1)*d)
    return sum
n,a,d=map(int,input().split())
print(ap(n,a,d))
