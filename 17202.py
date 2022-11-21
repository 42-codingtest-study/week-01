# 입력값 받기
a = list(map(int, input()))
b = list(map(int, input()))

# 배열 생성 및 초기화
result = []
for i in range(8):
    result.append(a[i])
    result.append(b[i])

# 결과가 두 자릿수가 아닐 때까지 인접한 수 더하기 반복
while len(result) > 2:
    temp = []
    for i in range(len(result) - 1):
        temp.append((result[i] + result[i + 1]) % 10)
    result = temp

print(result[0], result[1], sep='')