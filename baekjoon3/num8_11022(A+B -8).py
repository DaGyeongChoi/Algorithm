import sys
T=int(sys.stdin.readline())
for i in range(1,T+1):
    A,B=sys.stdin.readline().split()
    A=int(A)
    B=int(B)
    print("Case #",i,": ",A," + ",B," = ",A+B,sep='')