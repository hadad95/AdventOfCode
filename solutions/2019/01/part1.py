with open('./input', 'r') as f:
    inputs = f.read().strip().split('\n')
    
result = 0
for fuel in inputs:
    result += int(fuel) // 3 - 2

print(result)
