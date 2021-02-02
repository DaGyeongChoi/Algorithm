import sys
from collections import Counter

n=int(sys.stdin.readline())
num=[]
for i in range(n):
    num.append(int(sys.stdin.readline()))

#average
avr=sum(num)/n
print(round(avr))

#middle
num.sort()
print(num[n//2])

#mode
mode=Counter(num).most_common() #[(최빈값,최빈값의 빈도수), (두번째 최빈값, 두번째 최빈값의 빈도수) ,,,]
if(len(mode)==1):
    print(mode[0][0])
else:
    if(mode[0][1]==mode[1][1]):
        print(mode[1][0])
    else:
        print(mode[0][0])
#range
print(max(num)-min(num))