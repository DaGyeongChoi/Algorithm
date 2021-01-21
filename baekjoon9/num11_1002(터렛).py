T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    dis=((x2-x1)**2+(y2-y1)**2)**0.5
    r=[dis,r1,r2]
    m=max(r)
    r.remove(m)
    if(r1==r2 and dis==0):
        print("-1")
    elif(r1+r2==dis or r[0]+r[1]==m):
        print("1")
    elif(dis>=r1+r2 or sum(r)<=m):
        print("0")
    else:
        print("2")
