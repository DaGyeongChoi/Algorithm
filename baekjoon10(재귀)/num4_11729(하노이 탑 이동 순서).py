n=int(input())

def hanoi(n,start,mid,end):
    order = []
    if(n==1):
        print(start,end)
    else:
        hanoi(n-1,start,end,mid) #n-1개의 원판을 중간에 놓고 젤 큰 원판을 3으로 옮김
        print(start,end)
        hanoi(n-1,mid,start,end) #그 다음 중간의 원판을 3으로 옮긴다.

print((2**n)-1)
hanoi(n,1,2,3)
