n=int(input())
for i in range(1,n+1):
    if(i==n):
        print(0)
    else:
        i=str(i)
        con=list(i)
        i=int(i)
        sum=0
        for j in con:
            j=int(j)
            sum=sum+j #i의 각 자리 숫자 더하고
        sum=sum+i #i더해줘서 값계산, 이때 i가 생성자가 된다.

        if(sum==n):
            print(i)
            break