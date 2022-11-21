# 입력값 받기
n = int(input())

# 배열 생성 및 초기 세팅
fibo = [0 for _ in range(n + 1)]
fibo[0], fibo[1] = 0, 1

# 피보나치
for i in range(2, n + 1):
    fibo[i] = fibo[i - 2] + fibo[i - 1]

print(fibo[n])