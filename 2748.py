# https://www.acmicpc.net/problem/2748

n = int(input())
pibo = [0, 1]	# 초기값 설정
i = len(pibo)
while (i < n + 1) :
    pibo.append(pibo[i - 1] + pibo[i - 2])	# 피보나치의 규칙
    i += 1
print(pibo[n]);