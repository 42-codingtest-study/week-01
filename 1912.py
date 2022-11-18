n = int(input())
n_list = list(map(int,input().split()))

now = 0
Max = -1001
for i in n_list:
    if now < 0 and now < i: 
        now = i
    else: 
        now += i
    if Max < now: 
        Max = now
print(Max)
        

