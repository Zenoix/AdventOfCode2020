# import deepcopy to make changes in the seats
from copy import deepcopy


# function to create a list from input
def handle_input() -> list[list[str]]:
    with open("input.txt", "r") as f:
        # read in the input file as create a list without \n
        output = f.read().splitlines()

    # return the list as nested lists with the seats as items in the inner list
    return list(map(list, output))


def solution(seats: list[list[str]], vis_occ_seats: int) -> int:
    # number of row and columns
    num_rows = len(seats)
    num_cols = len(seats[0])

    # loop forever until break
    while True:
        # make a deepcopy of seats as we only check seats after all switch
        new_seats = deepcopy(seats)
        # bool to see if any changes are made
        change = False
        # loop through rows
        for row in range(num_rows):
            # loop through columns
            for col in range(num_cols):
                # if the "seat" is the floor then continue
                # (not needed but I thought would save time)
                if seats[row][col] == ".":
                    continue

                # number of adjacent occupied seats
                num_occ = 0

                # loop though each of the adjacent seats by y
                for row_offset in (-1, 0, 1):
                    # loop though each of the adjacent seats by x
                    for col_offset in (-1, 0, 1):
                        # if there is no offset (original seat), continue
                        if row_offset == 0 and col_offset == 0:
                            continue

                        # the indexes of the seats to check with the offsets
                        check_row = row + row_offset
                        check_col = col + col_offset

                        # <-- while loop block for part 2 only -->
                        # while inside the boundaries and the "seat" is floor
                        while 0 <= check_row < len(seats) and \
                                0 <= check_col < len(seats[0]) and \
                                seats[check_row][check_col] == "." and \
                                vis_occ_seats == 5:
                            # continue checking in that direction
                            check_row += row_offset
                            check_col += col_offset

                        # if the seat is within bounds and it is occupied
                        if 0 <= check_row < len(seats) and \
                                0 <= check_col < len(seats[0]) and \
                                seats[check_row][check_col] == "#":
                            num_occ += 1
                # if the seat is empty and there are no adj occupied seats
                if seats[row][col] == "L" and num_occ == 0:
                    # replace with "#" and set change to True (change made)
                    new_seats[row][col] = "#"
                    change = True
                # if the seat is occupied and at least vis_occ_seats occupied
                elif seats[row][col] == "#" and num_occ >= vis_occ_seats:
                    # replace with "L" and set change to True (change made)
                    new_seats[row][col] = "L"
                    change = True

        # if there has been no change in the latest check stop the while loop
        if change is False:
            break
        # else replace seats with new_seats
        seats = deepcopy(new_seats)

    # when the loop is broken we sum the number of "#" in the lists
    total = sum(row.count("#") for row in seats)

    return total


# driver code
if __name__ == "__main__":
    # get the list of lists of seats
    seats = handle_input()

    print("Part 1:", solution(seats, 4))
    print("Part 2:", solution(seats, 5))
