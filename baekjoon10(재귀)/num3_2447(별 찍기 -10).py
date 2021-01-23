def star(N,arr):
    if(N<3):
        return
    elif(N==3):
        arr[1][1]=" "
    else:
        star(N//3,arr)
        #for i in range(1,N,3): #N==3일때 별 중앙 비우기
         #   for j in range(1,N,3):
          #      arr[i][j] = " " 여기 범위설정을 좀 다르게 하면 될거같은데..

        for i in range(1,N // 3):
            for j in range(1,N // 3):
                if arr[i][j] == " ":  # 하나의 빈칸에서 파생되는 빈칸들
                    arr[i][j + N // 3] = " "
                    arr[i][j + 2 * N // 3] = " "
                    arr[i + N // 3][j] = " "
                    arr[i + N // 3][j + 2 * N // 3] = " "
                    arr[i + 2 * N // 3][j] = " "
                    arr[i + 2 * N // 3][j + N // 3] = " "
                    arr[i + 2 * N // 3][j + 2 * N // 3] = " "
        for i in range(N):
            for j in range(N):
                if(N//3 <=i< N//3*2 and N//3 <=j< N//3*2):
                    arr[i][j] = " "

N=int(input())
arr=[['*' for col in range(N)] for row in range(N)]
star(N,arr)
for i in arr:
    for j in i:
        print(j, end="")
    print()