import math

with open('./input', 'r') as f:
    inputs = f.read().strip()

layers = []
for i in range(0, len(inputs), 25*6): # 150 is 25x6
    layers.append(inputs[i:i+25*6])

target_layer = None
fewest = math.inf

for layer in layers:
    num = layer.count('0')
    if num < fewest:
        fewest = num
        print(fewest)
        print(layer)
        target_layer = layer

print(f'Result: {target_layer.count("1") * target_layer.count("2")}')
