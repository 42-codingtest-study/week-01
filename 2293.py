# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1	# 초기값 설정
for i in lst:	# 반복문
    for j in range(1, k + 1):
        if j - i >= 0:	# 
            dp[j] += dp[j - i]
print(dp[k])