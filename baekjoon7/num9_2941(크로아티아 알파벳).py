'''ca=["c=","c-","dz=","d-","lj","nj","s=","z="]
word=input()
sum=0
for i in range(len(word)):
    if(word[i]=="c" and (word[i+1]=="=" or word[i+1]=="-")):
        sum+=1
        i+=2
    elif(word[i]=="d" and (word[i+1]=="z" or word[i+1]=="-")):
        sum+=1
        i+=2
    elif((word[i]=="l" or word[i]=="n") and word[i+1]=="j"):
        sum+=1
        i+=2
    elif((word[i]=="s" or word[i]=="z") and word[i+1]=="="):
        sum+=1
        i+=2
    else:
        sum+=1
print(sum)
'''

ca=["c=","c-","dz=","d-","lj","nj","s=","z="]
word=input()
for i in ca:
    word=word.replace(i,"*")
print(len(word))    
