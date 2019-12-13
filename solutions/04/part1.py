lo = 246540
hi = 787419

count = 0

for i in range(lo, hi + 1):
    num = str(i)
    cond1 = True
    cond2 = False
    
    for x in range(len(num) - 1):
        if int(num[x + 1]) < int(num[x]):
            cond1 = False
            break
        
        if num[x + 1] == num[x]:
            cond2 = True
    
    if cond1 and cond2:
        count += 1

print(count)
