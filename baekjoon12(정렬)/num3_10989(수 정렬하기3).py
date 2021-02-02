#내장라이브러리
import sys
n=int(sys.stdin.readline())
num=[0 for i in range(10001)]

for i in range(n):
    num[int(sys.stdin.readline())]+=1

for i in range(10001):
    if(num[i]>0):
        for j in range(num[i]):
            print(i)

#인덱스 설정을 잘못해서 계속 오류가 났다..!
#범위를 잘 확인하자...