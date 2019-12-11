with open('./input', 'r') as f:
    lines = f.read().strip()
    
#lines = 'R8,U5,L5,D3\nU7,R6,D4,L4'

(line1, line2) = lines.split('\n')
points1 = []
intersections = []

currentx = 0
currenty = 0

for point in line1.split(','):
    val = int(point[1:])
    for i in range(val):
        if point[0] == 'R':
            currentx += 1
        elif point[0] == 'L':
            currentx -= 1
        elif point[0] == 'U':
            currenty += 1
        elif point[0] == 'D':
            currenty -= 1
        
        points1.append((currentx, currenty))

currentx = 0
currenty = 0

print(len(points1))

x = 0
for point in line2.split(','):
    val = int(point[1:])
    for i in range(val):
        x += 1
        if point[0] == 'R':
            currentx += 1
        elif point[0] == 'L':
            currentx -= 1
        elif point[0] == 'U':
            currenty += 1
        elif point[0] == 'D':
            currenty -= 1
        
        if (currentx, currenty) in points1:
            intersections.append((currentx, currenty))
            print(f'Intersection: {currentx}, {currenty}. Steps: {points1.index((currentx, currenty)) + 1 + x}')

print(intersections)
