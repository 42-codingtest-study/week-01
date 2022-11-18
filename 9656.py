n = int(input())

count = 0
while n > 0:
    if n < 4:
        n -= 1
        count += 1
    else :
        n -= 3
        count += 1
    
if count % 2 == 0:
    print("SK")
else:
    print("CY")