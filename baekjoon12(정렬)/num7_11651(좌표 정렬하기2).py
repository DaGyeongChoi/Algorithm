n=int(input())
location=[]

for i in range(n):
    x,y=map(int,input().split())
    location.append([x,y])
location.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(location[i][0],location[i][1])
