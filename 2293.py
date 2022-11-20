# https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
answer = 0
for i in range(len(lst)) :
    for j in range(i) :
        if ()