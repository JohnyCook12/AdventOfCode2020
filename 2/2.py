
"""
1. ukol (funkcni)


# read input:

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]


# get data from list:

policies = [x.split(':')[0] for x in mylist]
letters = [x.split(' ')[1] for x in policies]
numbers = [x.split(' ')[0] for x in policies]
times_min = [x.split('-')[0] for x in numbers]
times_max = [x.split('-')[1] for x in numbers]
passwords = [str(x.split(':')[1]).strip() for x in mylist]

all_data_list = zip(passwords,letters,times_min,times_max)


# count the valid passwords:

valid_passwords = 0

for password, letter, min, max in all_data_list:
    times_occured = password.count(letter)

    if (int(min) <= times_occured <= int(max)):
        valid = True
        valid_passwords += 1
    else:
        valid = False

print(valid_passwords)
"""


"""
2. ukol (funkcni)
"""

# read input:

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]


# get data from list:

policies = [x.split(':')[0] for x in mylist]
letters = [x.split(' ')[1] for x in policies]
numbers = [x.split(' ')[0] for x in policies]
times_min = [x.split('-')[0] for x in numbers]
times_max = [x.split('-')[1] for x in numbers]
passwords = [str(x.split(':')[1]).strip() for x in mylist]

all_data_list = zip(passwords,letters,times_min,times_max)


# count the valid passwords:

valid_passwords = 0
myindex = 0
for password, letter, first, second in all_data_list:
    myindex += 1
    print(myindex)

    if (letter == password[int(first)-1]) ^ (letter == password[int(second)-1]):
        print(True)
        valid_passwords += 1
    else:
        print(False)



print("Valid passwords: ", valid_passwords)

