
"""
1. ukol ()
"""
from collections import defaultdict
import copy
import time
start_time = time.time()            # TIMER - for lenth of execution



puzzle_input = [1,0,15,2,10,13]

list_of_results = copy.deepcopy(puzzle_input)


print(list_of_results)


for i in range(6,3001):
    last_number = list_of_results[-1]
    last_index = list_of_results[-1]

    age = 1
    for a in list_of_results[slice(-2,None,-1)]:
        if a == last_number:
            list_of_results.append(age)
            break
        else:
            age += 1

    if age >=  len(list_of_results):
        list_of_results.append(0)

print(list_of_results)
print(list_of_results[-1])




print("time elapsed: {:.2f}s".format(time.time() - start_time))          # TIMER - displays execution time