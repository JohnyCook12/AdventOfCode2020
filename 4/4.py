
"""1. ukol ()
- přečte input seznam pasportů
- zjistí kolik jich je validních (mají všechny údaje kromě CID)
údaje:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

"""

# read input:

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
    mylist2 = []
    temp_list = []

    mylist3 = []
    for line in mylist:                        # rozdělí input podle řádků a mezer do listu listů (tj. list passportů, kde passport je list údajů)
        line_data = line.split(' ')
        for data in line_data:
            mylist2.append(data)

    for x in mylist2:
        if x == '':
            mylist3.append(temp_list)
            temp_list = []
        else:
            temp_list.append(x)



    mylist4 = []
    for passport in mylist3:                    # udělá z toho list slovníků - každý slovník je passport
        names = []
        values = []
        for x in passport:
            name = x.split(':')[0]
            value = x.split(':')[1]
            names.append(name)
            values.append(value)
        passport_updated = dict(zip(names,values))
        mylist4.append(passport_updated)


    mylist4_status = []
    valid_passports = 0
    invalid_passports = 0
    for passport in mylist4:
        if ('byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport):
            mylist4_status.append('valid')
            valid_passports += 1
        else:
            mylist4_status.append('0')
            invalid_passports += 1
    print("first check (contain all fields except CID?): ")
    print('valid: ', valid_passports)
    print('invalid: ', invalid_passports)
    print("")
    print("second check (data validity): ")


    # data - validity check (druhy ukol)

    mylist4_data_validity = []
    data_valid_passports = 0

    hcl_valid_chars = "0123456789abcdef"
    ecl_valid_values = ['amb','blu','brn','gry','grn','hzl','oth']

    # kontrola

    for passport in mylist4:
        if ('byr' in passport) and (1920 <= int(passport.get('byr')) <=2002):
            if ('iyr' in passport) and (2010 <= int(passport.get('iyr')) <= 2020):
                if ('eyr' in passport) and (2020 <= int(passport.get('eyr')) <= 2030):
                    if ('hgt' in passport) and ((passport.get('hgt')[-2:] == 'in' and 59 <= int((passport.get('hgt')[:-2])) <= 76 ) or (passport.get('hgt')[-2:] == 'cm' and 150 <= int((passport.get('hgt')[:-2])) <= 193 )):
                        if ('hcl' in passport) and ( (passport.get('hcl')[0]=='#') and len(passport.get('hcl')[1:]) == 6 and all(c in hcl_valid_chars for c in passport.get('hcl')[1:])):
                            if ('ecl' in passport) and passport.get('ecl') in ecl_valid_values:
                                if ('pid' in passport) and len(passport.get('pid')) == 9:
                                    mylist4_data_validity.append("valid")
                                    data_valid_passports += 1

    print(mylist4_status)

    print('data valid: ', data_valid_passports)

"""
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
"""

