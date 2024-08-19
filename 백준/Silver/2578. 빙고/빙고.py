def check(arr):
    bingo = 0
    for i in range(5):
        if sum(arr[i]) == 0:
            bingo+=1
        if (arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i]+arr[4][i]) == 0:
            bingo+=1
    a=0
    b=0
    for i in range(5):
        a+= arr[i][i]
        b+= arr[4-i][i]
        
    if a == 0:
        bingo+=1
    if b==0:
        bingo+=1

    return bingo
arr=[] # 5/5
for i in range(5):
    arr.append(list(map(int,input().split())))

brr=[] # 1/25
for i in range(5):
    # brr.append(list(map(int,input().split())))
    brr += list(map(int,input().split()))

for i in range(25):
    x = brr[i]
    for a in range(5):
        for b in range(5):
            if arr[a][b] == x:
                arr[a][b] = 0
                break
    
    if check(arr)>=3:
        break

print(i+1)