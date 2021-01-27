n,m=map(int,input().split()) #n이 행
chess=[]
mini=[]
for i in range(n):
    chess.append(input())

for i in range(n-7):
    for j in range(m-7): #체스판을 8*8로 만들어줌
        #9*9보드에서 자를 수 있는 경우는 4가지, 10*10은 9가지...
        firstW=0
        firstB=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if(k+l)%2==0:
                    if chess[k][l]!='W':
                        firstW=firstW+1
                    if chess[k][l]!='B':
                        firstB=firstB+1
                else:
                    if chess[k][l] != 'B':
                        firstW = firstW + 1
                    if chess[k][l] != 'W':
                        firstB = firstB + 1
        mini.append(firstB)
        mini.append(firstW) #만들 수 있는 모든 8*8 배열 안에서 최소값을 찾아야하기 때문에 따로 리스트를 만들어 값들을 저장한다.

print(min(mini))
#리스트로 문자열 받고 문자열의 각 단어에 대해 이차원리스트처럼 바로 사용 가능

