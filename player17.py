def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return (a*b)//gcd(a,b)
a,b=map(int,input().split())
if a%b==0 or b%a==0:
    print(max(a,b))
else:
    print(lcm(a,b))
