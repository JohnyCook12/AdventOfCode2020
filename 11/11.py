
"""
1. ukol ()
1) Create function finding list of adjacent seats
2) Make loop that applies rules for occupying / emptying seats until situation become stable.
"""

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]

def adjacent_seats(row: int, seat: int, seats_list: list) -> list:
    seats_around = []

    # LEFT:
    if seat>0: seats_around.append(seats_list[row][seat-1])
    # RIGHT:
    if (len(seats_list[row])-1)>seat: seats_around.append(seats_list[row][seat+1])

    # seats_around.append(" ")

    # UPPER LEFT:
    if seat>0 and row>0: seats_around.append(seats_list[row-1][seat-1])
    # UPPER MIDDLE
    if row>0: seats_around.append(seats_list[row-1][seat])
    # UPPER RIGHT:
    if (len(seats_list[row])-1)>seat and row>0: seats_around.append(seats_list[row-1][seat+1])

    # seats_around.append(" ")

    # LOWER LEFT:
    if seat>0 and row<(len(seats_list)-1): seats_around.append(seats_list[row+1][seat-1])
    # LOWER MIDDLE
    if row<(len(seats_list)-1): seats_around.append(seats_list[row+1][seat])
    # LOWER RIGHT:
    if (len(seats_list[row])-1)>seat and row<(len(seats_list)-1): seats_around.append(seats_list[row+1][seat+1])

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
            if input_list[a][i]=='#' and adjacent_seats(a,i,input_list).count('#')>3: after_occupying_row.append('L')
            elif input_list[a][i]=='#' and adjacent_seats(a,i,input_list).count('#')<4: after_occupying_row.append('#')
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


all_result_lists, changes = whole_seating_process(mylist,150)

final_list = all_result_lists[-1]
total_occupied = 0
for i in final_list:
    total_occupied += i.count('#')

print('Occupied seats after process stabilizes: ',total_occupied)
print('Number of cycles when process becomes stabile: ',changes.count(1))

