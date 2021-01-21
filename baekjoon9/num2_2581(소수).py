M=int(input())
N=int(input())
arr=[]
for i in range(M,N+1):
    for j in range(2,i+1):
        if(i==j):
            arr.append(i)
        elif(i%j==0):
            break
sum=0
if(len(arr)==0):
    print("-1")
else:
    for i in arr:
        sum+=+i
    print(sum,min(arr))

