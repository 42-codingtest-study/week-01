# https://www.acmicpc.net/problem/13699

n = int(input())
dp = [0] * 36	# dp 배열 생성
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5	# 초기값 설정
for i in range(4, n + 1):
    t = 0
    if (i % 2):	# 홀수와 짝수가 규칙이 다르다
        for j in range(i // 2):
            t += 2 * dp[j] * dp[i - j - 1]
        dp[i] = t + dp[i // 2] ** 2	# 홀수일 경우 규칙 하나 더 생김
    else:
        for j in range(i // 2):
            t += 2 * dp[j] * dp[i - j - 1]
        dp[i] = t
print(dp[n])