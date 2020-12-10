
"""
1. ukol (funkcni)
"""


with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
sorted_mylist = sorted([int(c) for c in mylist])

charging_outlet = 0                             # given values
my_device_input = (max(sorted_mylist)+3)        # given values

sorted_mylist_with_ends = [charging_outlet] + sorted_mylist + [my_device_input]     # finally the list to process

diff_1_count,diff_2_count,diff_3_count = (0,0,0)

i=0
for i in sorted_mylist_with_ends:
    if i==(len(sorted_mylist_with_ends)-1):
        break
    diff = (i+1)-i
    if diff == 1:
        diff_1_count += 1
        i+=1
    elif diff == 2:
        diff_2_count += 1
        i+=1
    elif diff == 3:
        diff_3_count += 1
        i+=1
    elif diff > 3:
        print('Error: Difference too high!')
        i+=1
        break

print("Diff == 1: ",diff_1_count,",  Diff == 2: ",diff_2_count,",  Diff == 3: ",diff_3_count,", Diff1*Diff3 = ", diff_1_count*diff_3_count)
print(sorted_mylist_with_ends)



