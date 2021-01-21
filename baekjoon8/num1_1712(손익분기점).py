A,B,C=map(int,input().split())
c=0
if(B>=C):
    print("-1")
else:
    x=(A//(C-B))+1
    print(x)
'''
+1을 하지 않으면 x는 A+Bx=Cx일때를 가르키므로 +1을 해주어야한다.
우리가 구해야 하는 값은 Cx가 커질때니까!!
그리고 정수값 계산이니까 /가 아니라 //로 나누기
'''