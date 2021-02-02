#버블정렬
n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))

for j in range(n-1):
    for i in range(n-1):
        if(num[i]>num[i+1]):
            num[i],num[i + 1]=num[i+1],num[i]

for i in range(n):
    print(num[i])
