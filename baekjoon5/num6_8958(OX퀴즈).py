N = int(input())
for i in range(N):
    ox=list(input())
    score=0
    s=1
    for i in range(len(ox)):
        if(ox[i]=="O"):
            score=score+s
            s=s+1
        else:
            s=1
    print(score)