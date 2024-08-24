import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

def main():
    r,c,t = map(int,input().split())
    arr = [list(map(int,input().split()) )for _ in range(r)]
    
    def spread(arr,a,b): # 확산 1초
        arr_s = [[0 for i in range(c)] for j in range(r)]
        arr_s[a][0] = -1
        arr_s[b][0] = -1
        # 공기청정기, 벽 피해서 확산 a,0 b,0    0,0 r-1,c-1
        # 나머진 5분의 1만큼 더하기, 자신은 뺸 개수만큼 뺸 원래값을 더하기
        for i in range(r):
            for j in range(c):
                if arr[i][j] > 0:
                    spread_amount = arr[i][j] // 5
                    spread_count = 0
                    
                    # 상하좌우 확산
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                            arr_s[ni][nj] += spread_amount
                            spread_count += 1
                    
                    # 자신에게 남은 양 추가
                    arr_s[i][j] += arr[i][j] - spread_amount * spread_count
        
                    # arr_s[i-1][j] += arr[i][j]//5
                    # arr_s[i][j-1] += arr[i][j]//5
                    # arr_s[i+1][j] += arr[i][j]//5
                    # arr_s[i][j+1] += arr[i][j]//5
                    # arr_s[i][j] += arr[i][j] - ((arr[i][j]//5)*4) dltlqkf 이러지 말래...응
        
        return arr_s
    
    def wind(arr,a,b):
        # arr_w = [[0 for i in range(c)] for j in range(r)]
        # 공기청정기에 닿으면 삭제
        # 해당 칸을 기준으로 시계/반시계
        # 위칸 a,0
        # arr[a-1][0] = arr[a-2][0]
        # control = 0
        # con = [[-1,0,1,0],[0,1,0,-1]]
        # x,y=a-2,0
        # while 1:
        #     if x+con[0][control] <0 or x+con[0][control] >a or y+con[1][control] >=c: # 벽닿으면 회전
        #         control +=1
        #     if x+con[0][control]==a and y+con[1][control] <1: # 다음 칸이 청정기 닿으면 멈추기
        #         break
        #     arr[x][y] = arr[x+con[0][control]][y+con[1][control]] # 지금 칸 업데이트 : 다음 칸 값 고대로 가져오기
        for i in range(a - 1, 0, -1):
            arr[i][0] = arr[i - 1][0]
        for i in range(c - 1):
            arr[0][i] = arr[0][i + 1]
        for i in range(a):
            arr[i][c - 1] = arr[i + 1][c - 1]
        for i in range(c - 1, 1, -1):
            arr[a][i] = arr[a][i - 1]
        arr[a][1] = 0
            
        # 아래칸 b,0
        # arr[b+1][0] = arr[b+2][0]
        # control = 0
        # con = [[1,0,-1,0],[0,1,0,-1]]
        # x,y = b+2,0 # 현재 업데이트 해야 할 칸
        # while 1:
        #     if x+con[0][control] >=r or x+con[0][control] <b or y+con[1][control] >=c: # 벽닿으면 회전
        #         control +=1
        #     if x+con[0][control]==b and y+con[1][control] <1: # 다음 칸이 청정기 닿으면 멈추기
        #         break
        #     arr[x][y] = arr[x+con[0][control]][y+con[1][control]] # 지금 칸 업데이트 : 다음 칸 값 고대로 가져오기
        for i in range(b + 1, r - 1):
            arr[i][0] = arr[i + 1][0]
        for i in range(c - 1):
            arr[r - 1][i] = arr[r - 1][i + 1]
        for i in range(r - 1, b, -1):
            arr[i][c - 1] = arr[i - 1][c - 1]
        for i in range(c - 1, 1, -1):
            arr[b][i] = arr[b][i - 1]
        arr[b][1] = 0
        
        return arr
    
    # 공기청정기 위치 확인
    for i in range(r):
        if arr[i][0] == -1:
            air = [i,i+1]
            break
    
    
    for i in range(t):
        arr = spread(arr,air[0], air[1])
        arr = wind(arr,air[0], air[1])
    
    # 여기서 미세먼지 개수 구하기
    total_dust = sum(sum(row) for row in arr) + 2  # 공기청정기 -1 두 개
    print(total_dust)
    
if __name__ == "__main__":
    main()