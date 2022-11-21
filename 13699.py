# 입력값 받기
n = int(input())

# 배열 생성 및 초기화
dp = [0 for _ in range(n + 1)]
dp[0] = 1

# 값 저장해가며 찾기
for i in range(1, n + 1):
    r_idx = 0
    l_idx = i - 1
    while r_idx < i:
        dp[i] += dp[r_idx] * dp[l_idx]
        r_idx += 1
        l_idx -= 1

print(dp[n])