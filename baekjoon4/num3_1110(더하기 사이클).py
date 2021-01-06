N=int(input())
num=N
i=0
while True:
    num1=(num//10) + (num%10)
    num=str((num%10)) + str((num1%10))
    num=int(num)
    i=i+1
    if(num==N):
        print(i)
        break
