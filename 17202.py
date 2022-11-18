a = list(map(int, input()))
b = list(map(int, input()))
res = []

for i in range(len(a)):
    res.append(a[i])
    res.append(b[i])

while (len(res) != 2):
    tmp = []
    for i in range(len(res) -1):
        tmp.append((res[i] + res[i+1]) % 10)
    res = tmp

print(res[0], res[1], sep='')