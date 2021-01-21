T=int(input())
for i in range(T):
    H,W,N=map(int,input().split())
    x=1
    while True:
        if(H<N):
            x+=1
            N=N-H
        else:
            break
    if(N//10==0):
        print(N%10,x//10,x%10,sep="")
    else:
        print(N//10,N%10,x//10,x%10,sep="")


    room=0
    i=1
    if N<=H:
        room=N*100+1
        print(room)
    else:
        while N>H:
            N-=H
            i+=1
            if N<=H and i<=W:
                room=N*100+i
                print(room)
                break