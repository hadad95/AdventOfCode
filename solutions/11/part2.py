import sys

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
BLACK = 0
WHITE = 1

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

prog = Int(inputs)
grid = {}
current_pos = (0, 0)
grid[current_pos] = WHITE
current_dir = UP
total = 0

while not prog.halted:
    if current_pos not in grid:
        grid[current_pos] = BLACK
        total += 1

    prog.add_input(str(grid[current_pos]))
    new_color = prog.run()
    if new_color is None:
        break

    grid[current_pos] = int(new_color)
    rot = int(prog.run())
    if rot == 0:
        rot = -1
    current_dir = (rot + current_dir) % 4
    if current_dir == UP:
        current_pos = (current_pos[0], current_pos[1] + 1)
    elif current_dir == RIGHT:
        current_pos = (current_pos[0] + 1, current_pos[1])
    elif current_dir == DOWN:
        current_pos = (current_pos[0], current_pos[1] - 1)
    elif current_dir == LEFT:
        current_pos = (current_pos[0] - 1, current_pos[1])

output = ''
def lim_x(item):
    return item[0]

def lim_y(item):
    return item[1]

points = list(grid.keys())
max_x = max(points, key=lim_x)[0]
max_y = max(points, key=lim_y)[1]
min_x = min(points, key=lim_x)[0]
min_y = min(points, key=lim_y)[1]

for h in range(max_y, min_y - 1, -1):
    for w in range(min_x, max_x + 1):
        if (w, h) not in grid:
            grid[(w, h)] = BLACK
        
        if grid[(w, h)] == BLACK:
            sys.stdout.write(' ')
        else:
            sys.stdout.write('\u2588')
    
    sys.stdout.write('\n')
