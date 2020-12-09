
"""
1. ukol (funkcni)
- zjistit, jake je nejvyssi ID sedadla
- binarni cislovani sedadla. prvnich 7 znaku urcuje radu, posledni 3 sloupec (sedadlo)
- rada*8 + sloupec = ID sedadla
-
2. ukol (funkcni)
- najit ID meho sedadla.
- vim ze letadlo je plne, ale nektera ID cisla na zacatku a konci chybi (letadlo ma min nez 1024 mist)
"""

# read input:

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]

def seat_code_to_number(input: str) -> int:
    """
    converts BINARY to INT
    L = left, R = right. numbering starts from left
    """

    max = 2**len(input)
    index = 1
    final_number = 0
    for x in input:
        if x == 'R':
            final_number += (max/(2**(index)))
            index += 1
        elif x == 'L':
            index += 1
        else:
            raise Exception("invalid character in input")
    return int(final_number)

def row_code_to_number(input: str) -> int:
    """
    converts BINARY to INT
    F = front, B = rear. numbering starts from front
    """

    max = 2**len(input)
    index = 1
    final_number = 0
    for x in input:
        if x == 'B':
            final_number += (max/(2**(index)))
            index += 1
        elif x == 'F':
            index += 1
        else:
            raise Exception("invalid character in input")
    return int(final_number)

all_seats_list = list(range(1,1025))
occupied_seats_list = []

#print(all_seats_list)


for x in mylist:
    row_code = x[:7]
    seat_code = x[-3:]
    print(row_code_to_number(row_code))
    print(seat_code_to_number(seat_code))
    ID = (8*row_code_to_number(row_code)+seat_code_to_number(seat_code))
    occupied_seats_list.append(ID)
    print('ID: ', ID)
    print('')

all_seats_in_this_plane = list(range(min(occupied_seats_list),max(occupied_seats_list)+1))


print('All seats in this plane: ',all_seats_in_this_plane)

# finding my seat:
for i in occupied_seats_list:                   # vyházím z listu všech sedadel v letadle, všechna obsazená. zbyde moje
    all_seats_in_this_plane.remove(i)

print('Myseat: ',all_seats_in_this_plane)
# print(list(set(all_seats_list) - set(occupied_seats_list)))
print('Ocuupied seats total: ', len(mylist), ' Highest ID: ',max(occupied_seats_list), 'Lowest ID: ',min(occupied_seats_list))


