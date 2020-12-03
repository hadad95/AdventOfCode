with open('./input', 'r') as f:
    lines = f.read().strip().split('\n')

x = 0
result = 0
for line in lines:
    if line[x] == '#':
        result += 1
    
    x = (x + 3) % len(line)

print(result)