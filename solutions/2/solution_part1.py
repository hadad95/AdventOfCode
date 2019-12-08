with open('./input', 'r') as f:
    inputs = f.read().strip().split(',')

inputs = [int(i) for i in inputs] # convert the strings list to ints

""" Initializing the inputs """

inputs[1] = 12
inputs[2] = 2

cursor = 0

while True:
    opcode = inputs[cursor]
    if opcode == 99:
        print(inputs[0])
        break
        
    pos1 = inputs[cursor + 1]
    pos2 = inputs[cursor + 2]
    pos3 = inputs[cursor + 3]
    if opcode == 1:
        inputs[pos3] = inputs[pos1] + inputs[pos2]
    elif opcode == 2:
        inputs[pos3] = inputs[pos1] * inputs[pos2]
    else:
        print(f'INVALID OPCODE: {opcode}')
        
    cursor += 4
        
