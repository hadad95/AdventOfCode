with open('./input', 'r') as f:
    inputs = f.read().strip().split(',')

cursor = 0

while True:
    settings = inputs[cursor].rjust(5, '0')
    opcode = int(settings[-2:])
    if opcode == 99:
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
        inputs[param1] = input('Input: ')
        cursor += 2
    elif opcode == 4:
        param1 = int(inputs[cursor + 1])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        print(f'Output: {val1}')
        cursor += 2
    elif opcode == 5:
        param1 = int(inputs[cursor + 1])
        param2 = int(inputs[cursor + 2])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        val2 = int(inputs[param2]) if int(settings[-4]) == 0 else param2
        if val1 != 0:
            cursor = val2
        else:
            cursor += 3
    elif opcode == 6:
        param1 = int(inputs[cursor + 1])
        param2 = int(inputs[cursor + 2])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        val2 = int(inputs[param2]) if int(settings[-4]) == 0 else param2
        if val1 == 0:
            cursor = val2
        else:
            cursor += 3
    elif opcode == 7:
        param1 = int(inputs[cursor + 1])
        param2 = int(inputs[cursor + 2])
        param3 = int(inputs[cursor + 3])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        val2 = int(inputs[param2]) if int(settings[-4]) == 0 else param2
        val3 = int(inputs[param3]) if int(settings[-5]) == 0 else param3
        if val1 < val2:
            inputs[param3] = '1'
        else:
            inputs[param3] = '0'
        
        cursor += 4
    elif opcode == 8:
        param1 = int(inputs[cursor + 1])
        param2 = int(inputs[cursor + 2])
        param3 = int(inputs[cursor + 3])
        val1 = int(inputs[param1]) if int(settings[-3]) == 0 else param1
        val2 = int(inputs[param2]) if int(settings[-4]) == 0 else param2
        val3 = int(inputs[param3]) if int(settings[-5]) == 0 else param3
        if val1 == val2:
            inputs[param3] = '1'
        else:
            inputs[param3] = '0'
        
        cursor += 4
        
    else:
        print(f'INVALID OPCODE: {opcode}')
        
