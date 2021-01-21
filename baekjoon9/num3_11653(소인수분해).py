N=int(input())
i=2
arr=[]
while(i<N+1):
    if (i == N):
        arr.append(i)
        break
    elif(N%i==0):
        arr.append(i)
        N=N//i
        i=i
    else:
        i+=1
for i in arr:
    print(i)


