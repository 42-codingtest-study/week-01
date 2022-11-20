n = int(input())
res = [1, 1, 2]

for i in range(3, n+1):
    tmp = 0
    for j in range(i):
        tmp += res[j] * res[i-j-1]
    res.append(tmp)
print(res[n])