
"""
1. ukol ()
"""

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
timestamp = mylist[0]
buses = ['time']+[b for b in mylist[1].split(',') if b != 'x']
schedule = [buses,['0', '  D ', '  D ', '  D ', '  D ', '  D ', '  D ', '  D ', '  D ', '  D ']]        # FIRST LINES ARE DEFINED


for time in range(0,(int(timestamp)+50)):       # generating next lines:
    line = [time]
    for bus in buses[1:]:
        if time%int(bus) == 0: result = '  D '
        else: result = '  . '
        line.append(result)
    schedule.append(line)

for i in schedule:                              # display schedule
    print(i)

"""
RESULTS: 
first bus after timestamp = 827
waiting time = 5 min
multiplication = 4135
"""