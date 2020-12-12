
"""
2. ukol (funkcni)
"""
import math, numpy as np

with open("input.txt", "r") as myfile:
    mylist = [line[:-1] for line in myfile.readlines()]
    mylist2 = [(c[:1],c[1:]) for c in mylist]           # input list of (command, value)

after_move_waypoint = [(10,1)]          # list of waypoint positions after every waypoint move
after_move_ship = [(0,0)]               # list of ship positions after every ship move
ship_E = 0
ship_N = 0
waypoint_E = 10              # waypoint coordinates:
waypoint_N = 1               # waypoint coordinates:

def pol2cart(rho, phi):
    phi = phi * math.pi/180.0
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    phi = phi*180/math.pi
    return(rho, phi)

def move(command: str, value: str):
    global ship_E
    global ship_N
    global waypoint_E
    global waypoint_N

    value = int(value)

    if command == 'N': waypoint_N += value
    if command == 'S': waypoint_N -= value
    if command == 'E': waypoint_E += value
    if command == 'W': waypoint_E -= value

    if command == 'L':
        radius = cart2pol(waypoint_E, waypoint_N)[0]
        direction = cart2pol(waypoint_E, waypoint_N)[1]
        direction += value
        waypoint_E = int(round(pol2cart(radius, direction)[0]))
        waypoint_N = int(round(pol2cart(radius, direction)[1]))

    if command == 'R':
        radius = cart2pol(waypoint_E, waypoint_N)[0]
        direction = cart2pol(waypoint_E, waypoint_N)[1]
        direction -= value
        waypoint_E = int(round(pol2cart(radius, direction)[0]))
        waypoint_N = int(round(pol2cart(radius, direction)[1]))

    if command == 'F':                                      # MOVE SHIP
        ship_E += waypoint_E * value
        ship_N += waypoint_N * value
        after_move_ship.append((ship_E,ship_N))
    after_move_waypoint.append((waypoint_E, waypoint_N))


for i in mylist2:           # using the commands
    move(i[0],i[1])

print(mylist2)                  # commands list
print(after_move_waypoint)
print(after_move_ship)
manhatan_distance = abs(after_move_ship[-1][0]) + abs(after_move_ship[-1][1])
print(manhatan_distance)