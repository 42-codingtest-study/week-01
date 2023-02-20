# https://www.acmicpc.net/problem/1912

n = int(input())
lst = list(map(int, input().split()))	# 입력값 받아줌
dp = [0] * n	# dp 배열 생성
dp[0] = lst[0]	# 초기값 설정
for i in range(1, n) :
    dp[i] = max(lst[i], dp[i - 1] + lst[i])	# 부분합 구하기
print(max(dp))