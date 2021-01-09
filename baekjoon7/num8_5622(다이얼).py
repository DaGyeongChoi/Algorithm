alpha=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
grandma=list(input())
time=0

for j in grandma:
    for i in range(8):
        bet=list(alpha[i])
        if(j in bet):
            time+=i+3
            #num.append(i+2) #num리스트 생성하면 전화번호 출력할 수 있다.
print(time)