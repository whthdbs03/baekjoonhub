def main():
    n,m=map(int,input().split())
    arr=sorted(set(list(map(int,input().split()))))
    ans = [0 for i in range(m)]
    
    def recur(cur):
        if cur == m:
            print(*ans)
            return

        for i in range(len(arr)):
            ans[cur] = arr[i]
            recur(cur+1)
    
    recur(0)
    
if __name__ == "__main__":
    main()