with open('./input', 'r') as f:
    lines = f.read().strip().split('\n')

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1
for slope in slopes:
    trees = 0
    x = 0
    y = 0
    while y < len(lines):
        if lines[y][x] == '#':
            trees += 1
        
        x = (x + slope[0]) % len(lines[0])
        y += slope[1]
    
    result *= trees

print(result)