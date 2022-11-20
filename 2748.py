n = int(input())

tmp = [0, 1]

for _ in range(2, n+1):
    tmp.append(tmp[-1] + tmp[-2])    
print(tmp[-1])
    