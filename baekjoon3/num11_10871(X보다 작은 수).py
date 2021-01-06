N,X=map(int,input().split())

list1=list(sys.stdin.readline().split())
list1=[int(j) for j in list1]

for j in list1:
    if j<X:
        print(j,end=' ')


