#에라토스테네스의 체
def prime(N):
    prime_list=[True]*(N+1) #prime_list 초기화
    x=int((N+1)**0.5)   #N의 제곱근보다 작은 수의 배수들만 지워도 충분

    for i in range(2,x+1):
        if (prime_list[i]==True):
            for j in range(i+i,N+1,i):
                prime_list[j]=False
    return prime_list

T=int(input())
for i in range(T):
    a,b=0,0
    N=int(input())
    prime_list=prime(N)
    for i in range(N//2,N+1):
        if prime_list[i]==True and prime_list[N-i]==True:
            a,b=i,N-i
            print(b,a)
            break





