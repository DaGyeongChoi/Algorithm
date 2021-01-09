selfnum=[]
for n in range(1,10001):
    selfnum.append(n)   #selfnum에 정수 하나씩 추가

for i in range(1,10001):
    i=str(i)    #list 만드려고 str로 바꿔줌
    list_i=list(i)
    i = int(i)  #밑에 for문에서 계산해서 int로 다시 바꿔줌
    sum=0
    for j in list_i:
        j=int(j)
        sum=sum+j   #i의 각 자리 숫자 더하고
    sum=sum+i   #i더해줘서 값계산, 이때 i가 생성자가 된다.
    if(sum in selfnum):
        selfnum.remove(sum)

for n in range(len(selfnum)):
    print(selfnum[n])

#litst()의 인자로는 문자열, 튜플, 딕셔너리, range()함수 가능
#int는 넣을 수 없다.