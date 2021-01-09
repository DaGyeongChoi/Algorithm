c=int(input())
str=input()
n=list(str)
#split()은 ()안의 값을 기준으로 문자열을 나눠주는것->리스트에 저장
sum=0
for i in range(c):
    n[i]=int(n[i])
    sum=sum+n[i]
print(sum)
