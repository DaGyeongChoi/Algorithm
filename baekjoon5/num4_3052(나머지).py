num=[]
for i in range(10):
    num.append(int(input()))
    num[i]=num[i]%42
num=set(num)
print(len(num))

#set: 같은거끼리 묶어줌
