n=int(input())
l=list(map(int,input().split()))
m=int(len(l)/2)
if sum(l[:m])//len(l[:m]) == sum(l[m:])//len(l[m:]):
    print("yes")
else:
        print("no")
