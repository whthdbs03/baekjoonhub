#재제출
import sys
n = int(input())
nums = list(map(int,input().split()))
op = list(map(int,input().split()))

result = nums[0]
least = ""
most = ""

def dfs(num):
    global result, least, most
    if sum(op) == 0:
        if least == "":
            least = result
            # 값을 넣은 적이 없을 때 최초값을 정해준다.
            # 그냥 무작정 0 으로 하면 안된다.
        elif least > result:
            least = result

        if most == "":
            most = result
        elif most < result:
            most = result
        return
        
    for i in range(4):
        if op[i] > 0:
            preResult = result
            # 계산하기 전 이전 값을 미리 저장
            if i == 0:
                result += nums[num]
            elif i == 1:
                result -= nums[num]
            elif i == 2:
                result *= nums[num]
            else:
                result = int(result / nums[num])
            op[i] -= 1
                
            dfs(num+1)
            result = preResult
            # 부모 트리로 돌아왔으니 이전 값 대입
            op[i] += 1
            
dfs(1)
print(most,least,sep="\n")