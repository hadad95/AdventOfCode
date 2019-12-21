class Int():
    def __init__(self, inputs):
        self.inputs = inputs.copy()
        self.output = 0
        self.cursor = 0
        self.halted = False
        self.relative_base = 0
        self.ip = []
        self.input_callback = self.read_input
    
    def read_input(self):
        return str(self.ip.pop(0))
    
    def add_input(self, ip):
        self.ip.append(ip)
    
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
    
    def run(self):
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
                self.inputs[param1] = self.input_callback()
                self.cursor += 2
            elif opcode == 4:
                param1 = self.get_param(settings, 1)
                self.output = str(param1)
                self.cursor += 2
                #print(self.output)
                return self.output
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

inputs[0] = '2'
prog = Int(inputs)
blocks_count = 0
ball_loc = [0, 0]
paddle_loc = [0, 0]
score = 0

def read():
    if ball_loc[0] < paddle_loc[0]:
        return '-1'
    elif ball_loc[0] > paddle_loc[0]:
        return '1'
    else:
        return '0'

prog.input_callback = read

while not prog.halted:
    x = prog.run()
    y = prog.run()
    tile = prog.run()
    if x and y and tile:
        if int(x) == -1:
            score = int(tile)
        else:
            if int(tile) == 2:
                blocks_count += 1
            elif int(tile) == 3:
                paddle_loc = [int(x), int(y)]
            elif int(tile) == 4:
                ball_loc = [int(x), int(y)]

print(f'Score: {score}')
