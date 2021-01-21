T=int(input())
for i in range(0,T):
    F=int(input())
    N=int(input())
    arr=[]

    for i in range(0,N+1):
        arr.append(i)
    for j in range(F):
        for i in range(1,N+1):
            arr[i]+=arr[i-1]
    print(arr[N])


