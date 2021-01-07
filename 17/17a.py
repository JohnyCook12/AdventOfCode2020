
"""
Day 17
1. ukol (funkcni)
game of life
"""


import time
start_time = time.time()            # TIMER - for lenth of execution





with open("input.txt", "r") as myfile:                      # read input
    mylist = [line[:-1] for line in myfile.readlines()]


def whats_around(x:int, y:int, z:int) -> list:              # generates coordinates of all neighbours

    results = []

    for i in range(-1,2,1):
        for ii in range(-1,2,1):
            for iii in range(-1, 2, 1):
                if not (x+i,y+ii,z+iii) == (x,y,z):
                    results.append((x+i,y+ii,z+iii))
    return results


def step(alive_in: dict) -> dict:

    # 1): create map of neighbours count
    neighbours = {}
    for i in alive_in:
        generated_neighbours = whats_around(i[0],i[1],i[2])        # gets coordinates of ALL neighbours of each cell
        for a in generated_neighbours:                # makes map of neighbours count
            if a in neighbours:
                neighbours[a]+=1                      # increment counter if already in
            else:
                neighbours[a]=1                       # add to neighbours


    # 2): generate the output map from INPUT and NEIGHBOURS COUNT
    alive_out = {}
    for b in neighbours:
        if b in alive_in and 1 < neighbours[b] < 4:
            # alive_out.append(b)                       # output changed to dict (for lookup speed)
            alive_out[b]=0
        elif b in alive_in and (neighbours[b]<2 or neighbours[b]>3):
            pass
        elif b not in alive_in and neighbours[b] == 3:
            # alive_out.append(b)                       # output changed to dict (for lookup speed)
            alive_out[b]=0
        else:
            pass

    return alive_out



initial_state = []                              # just creating empty dicts
d0 = {}
d1 = {}
d2 = {}
d3 = {}
d4 = {}
d5 = {}
d6 = {}

x = 0
y = 0
z = 0

for i in mylist:                                # generate initial state list ()
    print(i)                                    # print given input
    for c in i:
        if c == '#':
            val = True
            initial_state.append((x, y, z))
        else: val = False
        if x == (len(i)-1): x = 0
        else: x += 1
    y += 1              # end of row

# print(initial_state)                            # displays initial state list
for a in initial_state:                         # create initial state dict
    d0[a]=0

d1 = step(d0)
d2 = step(d1)
d3 = step(d2)
d4 = step(d3)
d5 = step(d4)
d6 = step(d5)
# print(d6)                                     # print the map of alive cells (in stage 6)
print(len(d6))                                  # (TASK RESULT) - total count of alive cells






print("")
print("time elapsed: {:.2f}s".format(time.time() - start_time))          # TIMER - displays execution time