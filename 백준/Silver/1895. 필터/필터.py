import sys
input = sys.stdin.readline

ans=0
r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(list(map(int,input().split())))
t=int(input())

noise=[]
for i in range(r-2):
    for j in range(c-2):
        noise=sorted(arr[i][j:j+3]+arr[i+1][j:j+3]+arr[i+2][j:j+3])
        if noise[4]>=t:
            ans+=1
            
print(ans)