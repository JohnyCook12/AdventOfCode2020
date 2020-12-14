
"""
2. ukol (Not working with high numbers)
Works properly up to 12 digits numbers then just takes too much time.

    # execution times:
    # 9 - 10 zeros ... 4s
    # 10 - 11 zeros ... 40s
    # 11 - 12 zeros ... 400s

"""
import time
start_time = time.time()            # TIMER - for lenth of execution


with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]

timestamp_start =   1000000000
timestamp_end =     10000000000

def nearest_911_multiply(start: int) -> int:
    num = start
    while (num % 911 != 0):  # continues with first multiple of 911 from start
        num += 1
    return num

def generate_and_check(start: int, finish: int) -> str:
    num = start
    while num%911!=0:                 # continues with first multiple of 911 from start
        num += 1

    while num < finish:                 # check of the sequence
        if (num+31)%827==0:
            if (num-41)%41==0:
                if (num-6)%37==0:
                    if (num+13)%13==0:
                        if (num+14)%14==0:
                            if (num+23)%23==0:
                                if (num+29)%29==0:
                                    if (num+50)%19==0:
                                        print(f'Just found the sequence! Timestamp = {i-41}')
                                        exit()
        # print(f'{num} failed')
        num += 911
    print(f'For {start} - {finish} sequence NOT found. Last tested number was {num}')

generate_and_check(timestamp_start,timestamp_end)



print("time elapsed: {:.2f}s".format(time.time() - start_time))          # TIMER - displays execution time

