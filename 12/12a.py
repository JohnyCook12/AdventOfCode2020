
"""
1. ukol ()

1)
"""
import math, numpy as np

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
    mylist2 = [(c[:1],c[1:]) for c in mylist]           # input list of (command, value)

def pol2cart(rho, phi):
    phi = phi * math.pi/180.0
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

after_move = []

acctual_E = 0
acctual_N = 0
acctual_direction = 0

print(mylist2)

def move(command: str, value: str) -> (int, int, int):
    value = int(value)
    diff_E = acctual_E
    diff_N = acctual_N
    diff_F = acctual_direction
    if command == 'N': diff_N += value
    if command == 'S': diff_N -= value
    if command == 'E': diff_E += value
    if command == 'W': diff_E -= value

    if command == 'L': diff_F += value
    if command == 'R': diff_F -= value

    if command == 'F':
        diff_E += int(pol2cart(value, diff_F)[0])
        diff_N += int(pol2cart(value, diff_F)[1])

    return(diff_E, diff_N, diff_F)



for i in mylist2:
    difference = move(i[0],i[1])

    acctual_E = difference[0]
    acctual_N = difference[1]
    acctual_direction = difference[2]
    after_move.append(difference)

print(after_move)
final_distance = abs(after_move[-1][0])+abs(after_move[-1][1])
print(final_distance)