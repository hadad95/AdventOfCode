width = 25
height = 6
with open('./input', 'r') as f:
    inputs = f.read().strip()

layers = []
for i in range(0, len(inputs), width*height):
    layers.append(inputs[i:i+width*height])

result = ''
for i in range(width*height):
    pixel = ''
    for layer in layers:
        if layer[i] == '2':
            continue
        else:
            pixel = layer[i]
            break
    
    result += pixel

result = result.replace('0', ' ').replace('1', '\u2588')
rows = []
for i in range(0, len(result), width):
    rows.append(result[i:i+width])

print('\n'.join(rows))
