# https://www.acmicpc.net/problem/17202

A = list(map(int, input()))
B = list(map(int, input()))
answer = []
while (len(A) > 0) :
    answer.append(A.pop(0))
    answer.append(B.pop(0))
while (len(answer) != 2) :
    tmp = []
    for i in range(len(answer) - 1) :
        tmp.append((answer[i] + answer[i + 1]) % 10)
    answer = tmp
print(answer[0], answer[1], sep = '')