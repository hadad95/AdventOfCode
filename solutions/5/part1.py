with open('./input', 'r') as f:
    inputs = f.read().strip().split(',')

#inputs = [int(i) for i in inputs] # convert the strings list to ints

""" Initializing the inputs """

#inputs[1] = 12
#inputs[2] = 2

cursor = 0

while True:
    settings = inputs[cursor].rjust(5, '0')
    opcode = int(settings[-2:])
    if opcode == 99:
        print(inputs[0])
        break

    if opcode == 1:
        param1 = int(inputs[cursor + 1])
        param2 = int(inputs[cursor + 2])
        param3 = int(inputs[cursor + 3])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        val2 = int(inputs[param2]) if int(settings[-4]) == 0 else param2
        inputs[param3] = str(val1 + val2)
        cursor += 4
    elif opcode == 2:
        param1 = int(inputs[cursor + 1])
        param2 = int(inputs[cursor + 2])
        param3 = int(inputs[cursor + 3])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        val2 = int(inputs[param2]) if int(settings[-4]) == 0 else param2
        inputs[param3] = str(val1 * val2)
        cursor += 4
    elif opcode == 3:
        param1 = int(inputs[cursor + 1])
        inputs[param1] = int(input('Input: '))
        cursor += 2
    elif opcode == 4:
        param1 = int(inputs[cursor + 1])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        print(f'Output: {val1}')
        cursor += 2
    else:
        print(f'INVALID OPCODE: {opcode}')
        
