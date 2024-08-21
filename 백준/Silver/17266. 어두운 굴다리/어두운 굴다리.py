import sys
sys.setrecursionlimit(10000)   
import math

n=int(input()) # 굴다리길이
m=int(input()) # 가로등개수
x=list(map(int,input().split()))

ans = max(x[0], n- x[-1]) #적어도 출발지점에서 첫번째 가로등 적어도 끝에서 마지막 가로등

for i in range(1,m):
    if x[i-1] + ans*2 >= x[i]:
        continue
    else:
        ans= math.ceil((x[i] - x[i-1]) / 2)

print(ans)