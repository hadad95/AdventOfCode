class Int():
    def __init__(self, inputs):
        self.inputs = inputs.copy()
        self.original_inputs = inputs.copy()
        self.cursor = 0
        self.output = 0
        self.halted = False
    
    def run(self, ip):
        self.cursor = 0
        current_ip = 0
        self.inputs = self.original_inputs.copy()
        
        while True:
            settings = self.inputs[self.cursor].rjust(5, '0')
            opcode = int(settings[-2:])
            if opcode == 99:
                #print('HALT')
                self.halted = True
                break

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
                self.inputs[param1] = ip[current_ip]
                current_ip += 1
                self.cursor += 2
            elif opcode == 4:
                param1 = int(self.inputs[self.cursor + 1])
                val1 = int(self.inputs[param1]) if int(settings[-3]) == 0 else param1
                self.output = str(val1)
                self.cursor += 2
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

prog = Int(inputs)
total = 0

current_config = [0, 0, 0, 0, 0]
optimum_config = [0, 0, 0, 0, 0]

def calc(index, loop, ip):
    global total
    global optimum_config
    global current_config
    for i in loop:
        current_config[index] = i
        prog.run([str(i), ip])
        out = prog.output
        if index == 4:
            if int(out) > total:
                optimum_config = current_config.copy()
                total = int(out)
        else:
            l = loop.copy()
            l.remove(i)
            calc(index + 1, l, out)

calc(0, list(range(5)), '0')
print(total)
print(optimum_config)
