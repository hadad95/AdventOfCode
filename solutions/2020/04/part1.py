import re

with open('./input', 'r') as f:
    lines = f.read().strip().split('\n\n')

def is_int(i, base=10):
    try:
        int(i, base)
        return True
    except:
        return False

ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
result = 0
for line in lines:
    entries = re.split(r'\s+|\n', line)
    passport = {}
    for entry in entries:
        entry = entry.split(':')
        passport[entry[0]] = entry[1]
    
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
        if not(is_int(passport['byr']) and 1920 <= int(passport['byr']) <= 2002):
            continue
        if not(is_int(passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020):
            continue
        if not(is_int(passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030):
            continue
        if not(is_int(passport['pid']) and len(passport['pid']) == 9):
            continue
        if 'cm' in passport['hgt']:
            i = passport['hgt'][:-2]
            if not(is_int(i) and 150 <= int(i) <= 193):
                continue
        elif 'in' in passport['hgt']:
            i = passport['hgt'][:-2]
            if not(is_int(i) and 59 <= int(i) <= 76):
                continue
        else:
            continue
        if not(passport['hcl'][0] == '#' and len(passport['hcl']) == 7 and is_int(passport['hcl'][1:], base=16)):
            continue
        
        if not passport['ecl'] in ecl:
            continue
        result += 1

print(result)