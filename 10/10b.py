
"""
2. ukol (funkcni)

Solution is:
1) finding series of 3+ connectors with difference 1 together and write down its length.
2) For each serie count possible variants (based on its length). L=1: 2variants, L=2: 4variants, L=3: 7variants. (max length = 3)
3) Finally multiply the numbers together.
"""


with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
sorted_mylist = sorted([int(c) for c in mylist])

charging_outlet = 0                             # given values
my_device_input = (max(sorted_mylist)+3)        # given values

sorted_mylist_with_ends = [charging_outlet] + sorted_mylist + [my_device_input]     # finally the list to process

diff_1_count,diff_2_count,diff_3_count = (0,0,0)

#

lengths_of_variable_diff_1_series = []          # number of connectors in serie that can be altered
last_diff3_beginning = -1

i=0
for i in range(len(sorted_mylist_with_ends)):
    if i==(len(sorted_mylist_with_ends)-1):
        break
    diff = sorted_mylist_with_ends[i+1]-sorted_mylist_with_ends[i]
    if diff == 1:
        diff_1_count += 1
        i+=1
    elif diff == 2:
        diff_2_count += 1
        i+=1
    elif diff == 3:
        if i-last_diff3_beginning > 2:
            lengths_of_variable_diff_1_series.append(i-last_diff3_beginning-2)
        last_diff3_beginning = i

        diff_3_count += 1
        i+=1
    elif diff > 3:
        print('Error: Difference too high!')
        i+=1
        break

total_combinations = 1
for a in lengths_of_variable_diff_1_series:
    if a == 1:
        total_combinations = total_combinations * 2
    elif a == 2:
        total_combinations = total_combinations * 4
    elif a == 3:
        total_combinations = total_combinations * 7


print("Diff == 1: ",diff_1_count,",  Diff == 2: ",diff_2_count,",  Diff == 3: ",diff_3_count,", Diff1*Diff3 = ", diff_1_count*diff_3_count)
print(sorted_mylist_with_ends)
print("Lengths of variable series", lengths_of_variable_diff_1_series)
print("Total combinations: ", total_combinations)

