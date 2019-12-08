with open('./input', 'r') as f:
    strings = f.read().strip().split(',')

for i in range(100):
    for j in range(100):
        inputs = [int(i) for i in strings] # convert the strings list to ints

        """ Initializing the inputs """

        inputs[1] = i
        inputs[2] = j

        cursor = 0

        while True:
            opcode = inputs[cursor]
            if opcode == 99:
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
        
        if inputs[0] == 19690720:
            noun = inputs[1]
            verb = inputs[2]
            print(f'Noun: {noun}\nVerb: {verb}\nResult: {100 * noun + verb}')
            exit()
