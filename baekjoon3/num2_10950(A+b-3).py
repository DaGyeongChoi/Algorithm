T=int(input())
n=list() #비어있는 리스트 만들기
for i in range(0,T): #이 바보야..range를 써야지 범위가 설정되지
    A,B=input().split()
    A=int(A)
    B=int(B)
    n.append(A+B)
for i in range(0,T):
    print(n[i])