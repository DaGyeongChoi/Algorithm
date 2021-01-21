#에라토스테네스의 체 사용 -> 소수를 구하는 알고리즘
M,N=map(int,input().split())
prime_list=[True]*(N+1) #prime_list 초기화
x=int((N+1)**0.5)   #N의 제곱근보다 작은 수의 배수들만 지워도 충분

for i in range(2,x+1):
    if (prime_list[i]==True):
        for j in range(i+i,N+1,i):
            prime_list[j]=False

for i in range(M,N+1):
    if(M==1):
        prime_list[M]=False
    if(prime_list[i]==True):
       print(i)
#여기에는 1의 경우도 포함해줘야함(1이 True인 상태이기 때문에)

'''
여기는 range를 2부터로 설정해서 1의 경우 포함안해도 됨
arr=[]
for i in range(2,N+1):
    if(prime_list[i]==True):
        arr.append(i)
for i in range (len(arr)):
    if(arr[i]>=M):
        print(arr[i])
'''
