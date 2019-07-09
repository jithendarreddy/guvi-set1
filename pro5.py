kq=list(map(str,input()))
ab=dr=0
for i in range(0,len(kq)-1):
    bg=kq[i]
    if int(bg)!=0:
        for j in range(i+1,i+2):
            bg=bg+kq[j]
            if int(bg)<27 and int (bg)>0: ab=ab+1
            elif int(bg)==0: ab=ab-1
            else: break
if ab!=1: dr=ab%2
print(ab+dr+1)
