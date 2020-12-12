
"""
2. ukol (funkcni)

1) Update the function finding list of adjacent seats (with index_valid function)
2) Update occupying / unoccupying rules
3) Make loop that applies rules for occupying / emptying seats until situation become stable.
"""

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]

print(mylist)

def index_valid(row: int, seat: int, input: list) -> bool:
    if row in range(0, len(input)) and seat in range(0,len(input[row])):
        return True
    else:
        return False

def adjacent_seats(row: int, seat: int, seats_list: list) -> list:
    seats_around = []

    # LEFT:
    shift = 1
    while index_valid(row,seat-shift,seats_list):
        if seats_list[row][seat-shift] != '.':
            seats_around.append(seats_list[row][seat-shift])
            # positions.append('L')
            break
        elif seats_list[row][seat-shift] == '.':
            shift += 1

    # RIGHT:
    shift = 1
    while index_valid(row,seat+shift,seats_list):
        if seats_list[row][seat+shift] != '.':
            seats_around.append(seats_list[row][seat+shift])
            # positions.append('R')
            break
        elif seats_list[row][seat + shift] == '.':
            shift += 1


    # UPPER LEFT:
    shift = 1
    while index_valid(row-shift,seat-shift,seats_list):
        if seats_list[row - shift][seat - shift] != '.':
            seats_around.append(seats_list[row - shift][seat - shift])
            # positions.append('UL')
            break
        elif seats_list[row - shift][seat - shift] == '.':
            shift += 1

    # UPPER MIDDLE
    shift = 1
    while index_valid(row-shift,seat,seats_list):
        if seats_list[row - shift][seat] != '.':
            seats_around.append(seats_list[row - shift][seat])
            # positions.append('UM')
            break
        elif seats_list[row - shift][seat] == '.':
            shift += 1

    # UPPER RIGHT:
    shift = 1
    while index_valid(row-shift,seat+shift,seats_list):
        if seats_list[row - shift][seat + shift] != '.':
            seats_around.append(seats_list[row - shift][seat + shift])
            # positions.append('UR')
            break
        elif seats_list[row - shift][seat + shift] == '.':
            shift += 1

    # LOWER LEFT:
    shift = 1
    while index_valid(row+shift,seat-shift,seats_list):
        if seats_list[row + shift][seat - shift] != '.':
            seats_around.append(seats_list[row + shift][seat - shift])
            # positions.append('LL')
            break

        elif seats_list[row + shift][seat - shift] == '.':
            shift += 1

    # LOWER MIDDLE
    shift = 1
    while index_valid(row+shift,seat,seats_list):
        if seats_list[row + shift][seat] != '.':
            seats_around.append(seats_list[row + shift][seat])
            # positions.append('LM')
            break
        elif seats_list[row + shift][seat] == '.':
            shift += 1

    # LOWER RIGHT:
    shift = 1
    while index_valid(row+shift,seat+shift,seats_list):
        if seats_list[row + shift][seat + shift] != '.':
            seats_around.append(seats_list[row + shift][seat + shift])
            # positions.append('LR')
            break
        elif seats_list[row + shift][seat + shift] == '.':
            shift += 1

    return seats_around

def occupying(input_list: list) -> list:
    output_list = []
    for a in range(len(input_list)):
        after_occupying_row_string = ''
        after_occupying_row = []
        for i in range(len(input_list[a])):
            if input_list[a][i]=='L' and not '#' in adjacent_seats(a,i,input_list): after_occupying_row.append('#')
            if input_list[a][i]=='L' and '#' in adjacent_seats(a,i,input_list): after_occupying_row.append('L')
            if input_list[a][i]=='#': after_occupying_row.append('#')
            elif input_list[a][i]=='.': after_occupying_row.append('.')
        after_occupying_row_string = ('').join(after_occupying_row)
        output_list.append(after_occupying_row_string)
    return(output_list)

def unoccupying(input_list: list) -> list:
    output_list = []
    for a in range(len(input_list)):
        after_occupying_row_string = ''
        after_occupying_row = []
        for i in range(len(input_list[a])):
            if input_list[a][i]=='#' and adjacent_seats(a,i,input_list).count('#')>4: after_occupying_row.append('L')
            elif input_list[a][i]=='#' and adjacent_seats(a,i,input_list).count('#')<5: after_occupying_row.append('#')
            elif input_list[a][i]=='L': after_occupying_row.append('L')
            elif input_list[a][i]=='.': after_occupying_row.append('.')
        after_occupying_row_string = ('').join(after_occupying_row)
        output_list.append(after_occupying_row_string)
    return(output_list)

def whole_seating_process(input_list: list, iterations: int) -> tuple:
    output_list = [input_list]
    changes_list = [1]              # 0 means no changes compared to previous list, 1 means actual list is different than previous list
    occupied = 0

    for i in range(iterations):
        last_list = output_list[i]
        if occupied==0:
            output_list.append(occupying(last_list))
            occupied = 1
            if output_list[-1]==output_list[-2]: changes_list.append(0)
            else: changes_list.append(1)
        else:
            output_list.append(unoccupying(last_list))
            occupied = 0
            if output_list[-1]==output_list[-2]: changes_list.append(0)
            else: changes_list.append(1)

    return(output_list,changes_list)


all_result_lists, changes = whole_seating_process(mylist,100)

final_list = all_result_lists[-1]
total_occupied = 0
for i in final_list:
    total_occupied += i.count('#')
    print(i)


print('Occupied seats after process stabilizes: ',total_occupied)
print('Number of cycles when process becomes stabile: ',changes.count(1))

