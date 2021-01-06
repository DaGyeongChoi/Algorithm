N=int(input())
score=list(map(int,input().split()))
s_max=max(score)
for i in range(N):
    score[i]=(score[i]/s_max*100.0)
print(sum(score)/N)

