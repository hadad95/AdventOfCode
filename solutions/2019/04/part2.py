import re

exp = re.compile('(.)\\1+')

lo = 246540
hi = 787419

count = 0

for i in range(lo, hi + 1):
    num = str(i)
    cond1 = True
    cond2 = False
    
    for match in exp.finditer(num):
        if len(match[0]) == 2:
            cond2 = True
            break
    
    for x in range(len(num) - 1):
        if int(num[x + 1]) < int(num[x]):
            cond1 = False
            break
        """
        if x < 4 and num[x] == num[x + 1] and num[x] == num[x + 2]:
            cond2 = False
            break
        if num[x] == num[x + 1]:
            cond2 = True
        """
        
    if cond1 and cond2:
        count += 1

print(count)
