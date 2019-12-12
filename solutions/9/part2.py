class Int():
    def __init__(self, inputs):
        self.inputs = inputs.copy()
        self.output = 0
        self.cursor = 0
        self.halted = False
        self.relative_base = 0
        self.ip = []
    
    def check_bounds(self, index):
        if index >= len(self.inputs):
            self.inputs.extend(['0'] * (index - len(self.inputs) + 1))

    def get_param(self, settings, pos):
        mode = int(settings[(-1 * pos) - 2 ])
        if mode == 0:
            self.check_bounds(int(self.inputs[self.cursor + pos]))
            return int(self.inputs[int(self.inputs[self.cursor + pos])])
        elif mode == 1:
            return int(self.inputs[self.cursor + pos])
        elif mode == 2:
            self.check_bounds(int(self.inputs[self.cursor + pos]) + self.relative_base)
            return int(self.inputs[int(self.inputs[self.cursor + pos]) + self.relative_base])
    
    def get_location_param(self, settings, pos):
        mode = int(settings[(-1 * pos) - 2 ])
        if mode == 0:
            self.check_bounds(int(self.inputs[self.cursor + pos]))
            return int(self.inputs[self.cursor + pos])
        elif mode == 2:
            self.check_bounds(int(self.inputs[self.cursor + pos]) + self.relative_base)
            return int(self.inputs[self.cursor + pos]) + self.relative_base
    
    def run(self, ip):
        self.ip.append(ip)
        
        while True:
            settings = self.inputs[self.cursor].rjust(5, '0')
            opcode = int(settings[-2:])
            
            if opcode == 99:
                #print('HALT')
                self.halted = True
                return
                #return self.output

            elif opcode == 1:
                param1 = self.get_param(settings, 1)
                param2 = self.get_param(settings, 2)
                param3 = self.get_location_param(settings, 3)
                self.check_bounds(param3)
                self.inputs[param3] = str(param1 + param2)
                self.cursor += 4
            elif opcode == 2:
                param1 = self.get_param(settings, 1)
                param2 = self.get_param(settings, 2)
                param3 = self.get_location_param(settings, 3)
                self.check_bounds(param3)
                self.inputs[param3] = str(param1 * param2)
                self.cursor += 4
            elif opcode == 3:
                param1 = self.get_location_param(settings, 1)
                self.check_bounds(param1)
                self.inputs[param1] = str(self.ip.pop(0))
                self.cursor += 2
            elif opcode == 4:
                param1 = self.get_param(settings, 1)
                self.output = str(param1)
                self.cursor += 2
                print(self.output)
                #return self.output
            elif opcode == 5:
                param1 = self.get_param(settings, 1)
                param2 = self.get_param(settings, 2)
                if param1 != 0:
                    self.cursor = param2
                else:
                    self.cursor += 3
            elif opcode == 6:
                param1 = self.get_param(settings, 1)
                param2 = self.get_param(settings, 2)
                if param1 == 0:
                    self.cursor = param2
                else:
                    self.cursor += 3
            elif opcode == 7:
                param1 = self.get_param(settings, 1)
                param2 = self.get_param(settings, 2)
                param3 = self.get_location_param(settings, 3)
                self.check_bounds(param3)
                if param1 < param2:
                    self.inputs[param3] = '1'
                else:
                    self.inputs[param3] = '0'
                
                self.cursor += 4
            elif opcode == 8:
                param1 = self.get_param(settings, 1)
                param2 = self.get_param(settings, 2)
                param3 = self.get_location_param(settings, 3)
                self.check_bounds(param3)
                if param1 == param2:
                    self.inputs[param3] = '1'
                else:
                    self.inputs[param3] = '0'
                
                self.cursor += 4
            elif opcode == 9:
                param1 = self.get_param(settings, 1)
                self.relative_base += param1
                self.cursor += 2
                
            else:
                print(f'INVALID OPCODE: {opcode}')

with open('./input', 'r') as f:
    inputs = f.read().strip().split(',')

prog = Int(inputs)
prog.run('2')
