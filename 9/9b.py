"""
2. ukol (funkcni)
najit v inputu skupinu sousedicich cisel davajicich soucet 27911108 a určit součet největšího a nejmenšího z nich.
"""

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]

key = 27911108

i = 0
for i in range(len(mylist)):                    # start index of each serie
    sum_list = [int(mylist[i])]
    for a in range(i+1,len(mylist)):            # loop adding numbers (till the end of input) for each serie
        sum_list.append(int(mylist[a]))
        if sum(sum_list) == key:
            print(f'NUMBERS FOUND. Max = {max(sum_list)}, min = {min(sum_list)}, their sum is {max(sum_list)+min(sum_list)}')
            exit()
        elif sum(sum_list) > key:
            print(mylist[i+1])              # print the begining number of each group.
            sum_list = []
            break

print('not found :-( ')



