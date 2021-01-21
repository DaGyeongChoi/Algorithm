sugar=int(input())
bag=0

while(sugar>0):
    if(sugar%5==0):
        bag+=1
        sugar-=5
    elif(sugar%3==0):
        bag+=1
        sugar-=3
    elif(sugar>5):
        bag+=1
        sugar-=5
    else:
        bag=-1
        break
print(bag)
