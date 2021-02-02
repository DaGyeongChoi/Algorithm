n=int(input())
wlist=[]
wcnt=[]
for i in range(n):
    word=input()
    if word in wlist: #같은 단어가 리스트에 이미 있으면 리스트에 저장하지 않음
        continue
    else:
        wlist.append(word) #같은 단어가 없으면 리스트에 저장

wlist.sort() #단어를 사전 순으로 정렬
wlist.sort(key=lambda x:len(x)) #단어를 단어의 길이에 따라 정렬
for i in wlist:
    print(i)

#중복삭제를 위해 set 함수를 써도 됨됨