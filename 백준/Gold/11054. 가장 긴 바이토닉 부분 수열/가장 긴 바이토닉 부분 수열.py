import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 


def main():
    n = int(input())
    arr = list(map(int,input().split()))
    
    left = [1 for i in range(n)]
    right = [1 for i in range(n)]
    
    def update(i, start, end, step, arr, seq):
        for a in range(start, end, step):
            if arr[a] < arr[i] and seq[a] >= seq[i]:
                seq[i] = seq[a] + 1

    for i in range(1, n):
        update(i, 0, i, 1, arr, left)

    for i in range(n-2, -1, -1):
        update(i, i+1, n, 1, arr, right)
        
    ans = 0
    for i in range(n):
        ans = max(ans, left[i]+right[i]-1)
    
    print(ans)
    
    
if __name__ == "__main__":
    main()
