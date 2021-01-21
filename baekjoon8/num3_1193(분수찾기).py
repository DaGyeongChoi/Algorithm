x=int(input())
order=1
sum,A,B=0,0,0

while True:
    if (x <= sum):
        order=order-1
        if (order % 2 == 0):
            A = 1
            B = order
            for i in range(sum - order, x-1):
                A += 1
                B -= 1
            break
        elif(order % 2 != 0):
            A = order
            B = 1
            for i in range(sum - order, x-1):
                A -= 1
                B += 1
            break
    else:
        sum=sum+order
        order += 1

print(A,"/",B,sep="")