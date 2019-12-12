from itertools import permutations

class Int():
    def __init__(self, inputs):
        self.inputs = inputs.copy()
        self.output = 0
        self.cursor = 0
        self.halted = False
        self.ip = []
    
    def run(self, ip):
        self.ip.append(ip)
        
        while True:
            settings = self.inputs[self.cursor].rjust(5, '0')
            opcode = int(settings[-2:])
            #print(self.ip)
            if opcode == 99:
                #print('HALT')
                self.halted = True
                return self.output

            elif opcode == 1:
                param1 = int(self.inputs[self.cursor + 1])
                param2 = int(self.inputs[self.cursor + 2])
                param3 = int(self.inputs[self.cursor + 3])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                val2 = int(self.inputs[param2]) if int(settings[-4]) == 0 else param2
                self.inputs[param3] = str(val1 + val2)
                self.cursor += 4
            elif opcode == 2:
                param1 = int(self.inputs[self.cursor + 1])
                param2 = int(self.inputs[self.cursor + 2])
                param3 = int(self.inputs[self.cursor + 3])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                val2 = int(self.inputs[param2]) if int(settings[-4]) == 0 else param2
                self.inputs[param3] = str(val1 * val2)
                self.cursor += 4
            elif opcode == 3:
                param1 = int(self.inputs[self.cursor + 1])
                self.inputs[param1] = str(self.ip.pop(0))
                self.cursor += 2
            elif opcode == 4:
                param1 = int(self.inputs[self.cursor + 1])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                self.output = str(val1)
                self.cursor += 2
                return self.output
            elif opcode == 5:
                param1 = int(self.inputs[self.cursor + 1])
                param2 = int(self.inputs[self.cursor + 2])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                val2 = int(self.inputs[param2]) if int(settings[-4]) == 0 else param2
                if val1 != 0:
                    self.cursor = val2
                else:
                    self.cursor += 3
            elif opcode == 6:
                param1 = int(self.inputs[self.cursor + 1])
                param2 = int(self.inputs[self.cursor + 2])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                val2 = int(self.inputs[param2]) if int(settings[-4]) == 0 else param2
                if val1 == 0:
                    self.cursor = val2
                else:
                    self.cursor += 3
            elif opcode == 7:
                param1 = int(self.inputs[self.cursor + 1])
                param2 = int(self.inputs[self.cursor + 2])
                param3 = int(self.inputs[self.cursor + 3])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                val2 = int(self.inputs[param2]) if int(settings[-4]) == 0 else param2
                val3 = int(self.inputs[param3]) if int(settings[-5]) == 0 else param3
                if val1 < val2:
                    self.inputs[param3] = '1'
                else:
                    self.inputs[param3] = '0'
                
                self.cursor += 4
            elif opcode == 8:
                param1 = int(self.inputs[self.cursor + 1])
                param2 = int(self.inputs[self.cursor + 2])
                param3 = int(self.inputs[self.cursor + 3])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                val2 = int(self.inputs[param2]) if int(settings[-4]) == 0 else param2
                val3 = int(self.inputs[param3]) if int(settings[-5]) == 0 else param3
                if val1 == val2:
                    self.inputs[param3] = '1'
                else:
                    self.inputs[param3] = '0'
                
                self.cursor += 4
                
            else:
                print(f'INVALID OPCODE: {opcode}')

with open('./input', 'r') as f:
    inputs = f.read().strip().split(',')

result = 0
for perm in permutations(['5', '6', '7', '8', '9']):
    out = '0'
    progs = []
    for i in range(5):
        progs.append(Int(inputs))
        progs[i].ip.append(perm[i])

    while progs[-1].halted == False:
        for prog in progs:
            out = prog.run(out)
    
    result = max(result, int(out))

print(result)
