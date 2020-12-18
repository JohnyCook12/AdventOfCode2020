"""
2.ukol (funkcni)
"""


import time
start_time = time.time()            # TIMER - for lenth of execution


list_values = [1,0,15,2,10,13]
unique_numbers = {1:1,0:2,15:3,2:4,10:5}


def series_append(serie: list, dictionary: dict, l):
    if unique_numbers.get(list_values[l-1]) == None:
        list_values.append(0)
    else:
        # list_values[i - 1] in unique_numbers:
        list_values.append(l - unique_numbers[list_values[-1]])          # adds number to list
    unique_numbers[list_values[-2]] = l


for i in range(6, 30000000):
    series_append(list_values,unique_numbers,i)


print(list_values)
print("time elapsed: {:.2f}s".format(time.time() - start_time))          # TIMER - displays execution time