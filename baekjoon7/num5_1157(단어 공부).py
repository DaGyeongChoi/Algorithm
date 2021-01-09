word=str(input())
word=word.upper()    #대문자로
wordlist=list(set(word))    #받은 word에서 같은 알파벳 제거를 위해 set()
cnt=[]
for i in range(len(wordlist)):
    cnt.append(word.count(wordlist[i])) #wordlist의 알파벳 가지고 word에서 그 개수 찾기

if cnt.count(max(cnt))>=2:  #cnt의 max의 개수가 두 개 이상이면
    print("?")
else:
    '''print(wordlist)
    print(cnt)
    print(max(cnt))
    print(cnt.index(max(cnt)))'''
    print(wordlist[cnt.index(max(cnt))])
    #(cnt의 max) 값의 위치를 find로 찾고 wordlist에서 출력
#리스트에서는 index
#문자열에서는 find