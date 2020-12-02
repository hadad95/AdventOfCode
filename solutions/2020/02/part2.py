with open('./input', 'r') as f:
    inputs = f.read().strip().split('\n')

result = 0

for line in inputs:
    split = line.split(': ')
    password = split[1]
    split = split[0].split(' ')
    character = split[1]
    split = split[0].split('-')
    lo = int(split[0]) - 1
    hi = int(split[1]) - 1
    if (password[lo] == character) ^ (password[hi] == character):
        result += 1

print(result)