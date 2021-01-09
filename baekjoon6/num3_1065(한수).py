num=int(input())
cnt=0
for i in range(1,num+1):
    i=list(str(i))
    if(len(i)<=2):
        cnt+=1
    else:
        i=list(map(int,i))
        if(i[0]-i[1] == i[1]-i[2]):
         cnt+=1
print(cnt)

#1000은 어차피 등차수열 아니라서 포함 안해도 된다