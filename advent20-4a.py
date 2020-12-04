with open("advent20-4a-input.txt","r") as f:
    input = f.read().split('\n')
    del input[len(input) - 1]

def passport_dictionary(input):
    passports = {}
    pp_id = 0
    passports[pp_id] = ''
    for i in range(len(input)):
        if input[i] == '':
            pp_id += 1
            passports[pp_id] = ''
        else:
            passports[pp_id] += ' '
            passports[pp_id] += input[i]
    return passports

def check_passport(passport):
    requirements = [
                'byr:',
                'iyr:',
                'eyr:',
                'hgt:',
                'hcl:',
                'ecl:',
                'pid:'
    ]

    #print passport
    #print 'Birth Year'
    if requirements[0] in passport:
        byr = int(passport[passport.index(requirements[0]) + 4 : passport.index(requirements[0]) + 9])
        #print byr
    else:
        return False
    if byr > 1919 and byr < 2003:
        pass
    else:
        return False

    #print 'Issue Year'
    if requirements[1] in passport:
        iyr = int(passport[passport.index(requirements[1]) + 4 : passport.index(requirements[1]) + 9])
        #print iyr
    else:
        return False
    if iyr > 2009 and iyr < 2021:
        pass
    else:
        return False

    #print 'Expiration Year'
    if requirements[2] in passport:
        eyr = int(passport[passport.index(requirements[2]) + 4 : passport.index(requirements[2]) + 9])
        #print eyr
    else:
        return False
    if eyr > 2019 and eyr < 2031:
        pass
    else:
        return False

    #print 'Height'
    if requirements[3] in passport:
        hgt = passport[passport.index(requirements[3]) + 4 : passport.index(requirements[3]) + 9]
        #print hgt
    else:
        return False
    if hgt[-2:] == 'cm' and int(hgt[0:3]) > 149 and int(hgt[0:3]) < 194:
        pass
    else:
        hgt = hgt[0:4]
        if hgt[-2:] == 'in' and int(hgt[0:2]) > 58 and int(hgt[0:2]) < 77:
            pass
        else:
            return False


    #print 'Hair Colour'
    if requirements[4] in passport:
        hcl = passport[passport.index(requirements[4]) + 4 : passport.index(requirements[4]) + 11]
        #print hcl
    else:
        return False
    if hcl[0] == '#' and hcl[1:6].isalnum():
        pass
    else:
        return False


    #print 'Eye Colour'
    if requirements[5] in passport:
        ecl = passport[passport.index(requirements[5]) + 4 : passport.index(requirements[5]) + 7]
        #print ecl
    else:
        return False
    if ecl in 'amb blu brn gry grn hzl oth':
        pass
    else:
        return False

    #print 'Passport ID'
    if requirements[6] in passport:
        pid = passport[passport.index(requirements[6]) + 4 : passport.index(requirements[6]) + 14]
        if len(pid) < 9:
            return False
        try:
            pid = int(pid)
            #print pid
        except ValueError:
            return False
    else:
        return False
    #print pid
    if pid + 1 < 999999999:
        pass
    else:
        return False

    return True


counter = 0
for passport in passport_dictionary(input).values():
    counter += check_passport(passport)

print counter
