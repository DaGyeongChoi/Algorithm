n=int(input())
plus,sum,i=0,1,1    #i는 시작인 1도 세야하므로 1부터 시작

while True:
    if(n<=sum):
        print(i)
        break
    else:
        plus=6*i
        i += 1
        sum = sum + plus

