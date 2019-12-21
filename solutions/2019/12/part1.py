class Moon():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def apply_gravity(self, moon):
        self.vx += (moon.x - self.x) / abs(moon.x - self.x) if moon.x - self.x != 0 else 0
        self.vy += (moon.y - self.y) / abs(moon.y - self.y) if moon.y - self.y != 0 else 0
        self.vz += (moon.z - self.z) / abs(moon.z - self.z) if moon.z - self.z != 0 else 0
    
    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
    
    def get_pot(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
    
    def get_kin(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

moons = []
with open('./input', 'r') as f:
    lines = f.read().strip().split('\n')
    for line in lines:
        coords = line.strip()[1:-1].split(', ')
        x = int(coords[0][2:])
        y = int(coords[1][2:])
        z = int(coords[2][2:])
        moons.append(Moon(x, y, z))

for x in range(1000):
    for i in range(len(moons)):
        sub = list(range(len(moons)))
        sub.remove(i)
        for j in sub:
            moons[i].apply_gravity(moons[j])

    for i in range(len(moons)):
        moons[i].apply_velocity()

total = 0
for i in range(len(moons)):
    pot = moons[i].get_pot()
    kin = moons[i].get_kin()
    total += pot * kin

print(total)
