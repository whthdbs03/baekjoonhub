import sys
input = sys.stdin.readline
n = int(input())
arr = [-1] + list(map(int, input().split()))
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(1, n//b+1):
            if arr[i*b] == 0:
                arr[i*b] = 1
            else:
                arr[i*b] = 0
    if a == 2:
        if arr[b] == 0:
            arr[b] = 1
        else:
            arr[b] = 0
        l, r = b-1, b+1
        
        
        while l > 0 and r <= n and arr[l] == arr[r]:
            if arr[l] == 0:
                arr[l], arr[r] = 1,1
            else:
                arr[l], arr[r] = 0,0
            l = l - 1
            r = r + 1

for k in range(1,n+1):
    print(arr[k], end=" ")
    if k % 20 == 0:
        print()