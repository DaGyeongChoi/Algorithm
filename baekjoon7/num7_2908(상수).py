num=list(input().split())
A=num[0][::-1]
B=num[1][::-1]
if(A>B):
    print(A)
else:
    print(B)

#arr[::-1]을 사용하면 역순으로 입력 가능