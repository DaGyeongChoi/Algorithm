import math
A,B,V=map(int,input().split())
print(math.ceil((V-A)/(A-B))+1)


#1. 마지막엔 결국 A만큼 올라가게 되어있다.
#2. 그래서 V-A의 높이 만큼 A-B의 속도로 얼마나 걸리냐를 구하고 1을 더하면 된다.
#3. 소수점이 나올 경우 올림으로 처리한다.

'''
while True:
    day = day + 1
    high=high+A
    if (high >= V):
        break
    high=high-B
print(day)
이 코드는 시간초과..
'''
'''
import math
math.ceil()은 올림함수
math.floor()은 내림함수
math.round()는 반올림함수
'''