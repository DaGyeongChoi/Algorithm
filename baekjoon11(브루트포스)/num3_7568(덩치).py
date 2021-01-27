n=int(input())
person=[]
rank=[]

for i in range(n):
    height,weight=map(int,input().split())
    person.append((height,weight))

for i in range(n):
    score = 1
    for j in range(n):
        if(person[i][0]<person[j][0] and person[i][1]<person[j][1]):
            score+=1
    rank.append(score)

for i in rank:
    print(i,end=' ')


