g,h=map(str,input("").split())
if(len(g)!=len(h)):
    print("no")
d=[g.count(i) for i in g]
e=[h.count(i) for i in h]
if(d==e):
    print("yes")
else:
    print("no")
