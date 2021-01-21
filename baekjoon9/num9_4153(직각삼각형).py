while True:
    x,y,z=map(int,input().split())
    if(x==0 and y==0 and z==0):
        break
    else:
        tri=[x,y,z]
        hypo=max(x,y,z)
        tri.remove(hypo)
        if(hypo**2==tri[0]**2+tri[1]**2):
            print("right")
        else:
            print("wrong")
