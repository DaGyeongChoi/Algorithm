#에라토스테네스의 체 사용 -> 소수를 구하는 알고리즘
N=2*123456
prime_list=[True]*(N+1) #prime_list 초기화
x=int((N+1)**0.5)   #N의 제곱근보다 작은 수의 배수들만 지워도 충분
for i in range(2,x+1):
    if (prime_list[i]==True):
        for j in range(i+i,N+1,i):
            prime_list[j]=False

while True:
    n=int(input())
    if(n==0):
        break
    else:
        count=0
        for i in range(n+1,2*n+1):
            if(prime_list[i]==True):
                count+=1
    print(count)

'''
arr=[]
while True:
    n=int(input())
    if(n==0):
        break
    else:
        count = 0
        for i in range(n+1,2*n+1):
            for j in range(2,i+1):
                if(i==j):
                    count+=1
                elif(i%j==0):
                    break
        arr.append(count)
print(arr)
시간초과 뜨는 코드
'''