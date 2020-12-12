"""
---------------------------------My Conventions-----------------------------
North is up, East is right, South is down, West is left

Part 1:
- (E, N, W, S) -> (0 deg, 90 deg, 180 deg, 270 deg)

Part 2:
- Positions of ship and the waypoints will be vectors
- Ship will be a vector from 0, 0 (starting position)
- Waypoint will be vector from the center of the ship (relative to ship)
----------------------------------------------------------------------------
"""

# part 2 solution requires numpy
import numpy as np


# function to create a list from input
def handle_input() -> list[tuple]:
    with open("input.txt", "r") as f:
        # read in the input file as create a list without \n
        inp = f.read().splitlines()
    # create a list of tuples that contains the action and the values
    output = [(action[0], int(action[1:])) for action in inp]

    return output


# function to move the ship (part 1)
def move_ship(magnitude: int, direction: int, x: int, y: int) -> (int, int):
    # modifies the x, y coords of the ship depending on direction it's facing
    if direction == 0:
        return x + magnitude, y
    elif direction == 90:
        return x, y + magnitude
    elif direction == 180:
        return x - magnitude, y
    else:
        return x, y - magnitude


# part 1 code
def part_1() -> int:
    # set angle to 0 (starting direction: East)
    angle = 0
    # set starting coords to 0, 0
    x = y = 0

    nsew_to_deg = {"E": 0, "N": 90, "W": 180, "S": 270}

    # loop through actions and values
    for action, value in actions:
        if action == "F":
            x, y = move_ship(value, angle, x, y)
        elif action == "L":
            # add the angle (mod 360 in case it goes over 360 deg)
            angle = (angle + value) % 360
        elif action == "R":
            # minus the angle (mod 360 in case it goes under 0 deg)
            angle = (angle - value) % 360
        else:
            temp_angle = nsew_to_deg[action]
            x, y = move_ship(value, temp_angle, x, y)

    # return manhatten distance
    return abs(x) + abs(y)


# function to rotate the waypoint (part 2)
def rot_waypoint(waypoint, angle, right=False):
    # get the current x, y coords of the waypoint relative to ship
    x = waypoint[0]
    y = waypoint[1]
    # if it's rotating to the right, convert angle to counter-clockwise
    if right is True:
        angle = 360 - angle

    # rotate the waypoint relative to the ship using vector properties
    if angle == 90:
        return np.array([-y, x])
    elif angle == 180:
        return np.array([-x, -y])
    else:
        return np.array([y, -x])


# part 2 code
def part_2() -> int:
    # initialise ship's position vector and waypoint vectors
    position = np.array([0, 0])
    waypoint = np.array([10, 1])

    # loop through actions and values
    for action, value in actions:
        if action == "F":
            # scalar multiplication on waypoint and then add to position
            position += value * waypoint
        elif action == "N":
            # move waypoint up
            waypoint += np.array([0, value])
        elif action == "S":
            # move waypoint down
            waypoint += np.array([0, -value])
        elif action == "E":
            # move waypoint right
            waypoint += np.array([value, 0])
        elif action == "W":
            # move waypoint left
            waypoint += np.array([-value, 0])
        elif action == "L":
            waypoint = rot_waypoint(waypoint, value)
        elif action == "R":
            waypoint = rot_waypoint(waypoint, value, True)

    # return manhatten distance
    return abs(position[0]) + abs(position[1])


# driver code
if __name__ == "__main__":
    # get the actions from the input file
    actions = handle_input()

    print("Part 1:", part_1())
    print("Part 2:", part_2())
