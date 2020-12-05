with open('./input', 'r') as f:
    lines = f.read().strip().split('\n')

ids = []

for line in lines:
    row = 0
    col = 0
    rows = [x for x in range(128)]
    cols = [x for x in range(8)]
    for i in range(7):
        if line[i] == 'F':
            rows = rows[: int(len(rows) / 2)]
        elif line[i] == 'B':
            rows = rows[int((len(rows) + 1) / 2) :]
    
    row = rows[0]
    for i in range(7, 10):
        if line[i] == 'L':
            cols = cols[: int(len(cols) / 2)]
        elif line[i] == 'R':
            cols = cols[int((len(cols) + 1) / 2) :]
    
    col = cols[0]
    ids.append(row * 8 + col)

print(max(ids))