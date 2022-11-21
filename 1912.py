# 입력값 받기
n = int(input())
arr = list(map(int, input().split()))

# 배열 생성 및 초기화
dp = []
dp.append(arr[0])

# dp[i] + arr[i + 1]와 arr[i + 1] 중 더 큰 값을 저장하는 이유 : dp[i]가 음수일 경우
for i in range(n - 1):
    dp.append(max(dp[i] + arr[i + 1], arr[i + 1]))

print(max(dp))