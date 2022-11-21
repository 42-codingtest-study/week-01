# 입력값 받기
n = int(input())
arr = list(map(int, input().split()))

# 배열 생성 및 초기화
dp = [0 for _ in range(n)]
dp[0] = arr[0]

# dp[i - 1] + arr[i]와 arr[i] 중 더 큰 값을 저장하는 이유 : dp[i - 1]이 음수일 경우
for i in range(1, n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))