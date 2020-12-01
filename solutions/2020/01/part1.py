with open('./input', 'r') as f:
    inputs = [int(i) for i in f.read().strip().split('\n')]

for i in range(len(inputs)):
    for j in range(i+1, len(inputs)):
        if inputs[i] + inputs[j] == 2020:
            print(inputs[i] * inputs[j])
            exit()