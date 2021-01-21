n=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    for j in range(2,i+1):
        if(i==j):   #i와 j의 값이 같으면 소수
            count+=1
        elif(i%j==0):   #자기자신이 아닌 값으로 나누어지면 소수 아님
            break
print(count)
