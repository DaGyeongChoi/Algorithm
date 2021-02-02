n=int(input())
member=[]
for i in range(n):
    age,name=input().split()
    age=int(age)
    member.append((age,name))

member.sort(key=lambda x:x[0])

for i in range(n):
    print(member[i][0],member[i][1])