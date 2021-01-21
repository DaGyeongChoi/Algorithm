#이런문제내지마요~ 사실 규칙 100프로 이해 못함ㅠ
T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    distance=y-x
    count = 0   #이동횟수
    move = 1    #이동가능거리
    move_plus=0
    while move_plus < distance:
        count+=1
        move_plus+=move
        if (count%2==0):
            move+=1
    print(count)