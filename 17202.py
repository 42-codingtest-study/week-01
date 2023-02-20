# https://www.acmicpc.net/problem/17202

A = list(map(int, input()))
B = list(map(int, input()))
answer = []
while (len(A) > 0) :	# 두 배열을 하나의 배열로 만들어준다.
    answer.append(A.pop(0))
    answer.append(B.pop(0))
    
while (len(answer) != 2) :	# 배열의 크기가 2가 될 때까지 번호를 합쳐준다.
    tmp = []
    for i in range(len(answer) - 1) :
        tmp.append((answer[i] + answer[i + 1]) % 10)
    answer = tmp
print(answer[0], answer[1], sep = '')