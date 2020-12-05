# import libraries
import itertools
from typing import Union


# function to get the row from the code
def get_row(code: str, low: int, high: int) -> Union[int, str]:
    # using recursion
    if low == high:
        # return row number and the remaining code
        return low, code
    if code[0] == "F":
        return get_row(code[1:], low, (low + high)//2)
    else:
        return get_row(code[1:], (low + high)//2 + 1, high)


# function to get the column from the rest of the code
def get_col(code: str, low: int, high: int) -> int:
    # using recursion
    if len(code) == 0:
        # return seat number
        return low
    if code[0] == "L":
        return get_col(code[1:], low, (low + high)//2)
    else:
        return get_col(code[1:], (low + high)//2 + 1, high)


# function to find the row with a missing seat
def non_full_row(seats: dict) -> Union[int, list]:
    # question states our seat is not in the front or back
    front, back = min(seats.keys()), max(seats.keys())+1
    # delete rows of seats in the front and back
    for del_row in itertools.chain(range(front, 10), range(100, back)):
        del seats[del_row]

    # iterate through the rows
    for row in seats:
        existing_seats = seats[row]
        # check if row has missing seat
        if len(existing_seats) != 8:
            # return row number and the existing seats in row
            return row, existing_seats


# find the missing seat number
def missing_seat(cols: list) -> int:
    col = list(set(range(0, 8)) - set(cols))[0]
    return col


# calculate seat id
def seat_id(row: int, col: int) -> int:
    return row * 8 + col


# function to handle the input into a list of seat codes
def handle_input() -> list:
    with open("input.txt", "r") as f:
        return f.read().splitlines()


# part 1 driver code
def part_1(seat_codes: list) -> int:
    # set highest id to 0
    highest_id = 0

    for seat in seat_codes:
        # get row and column from seat code
        row, remaining_code = get_row(seat, 0, 127)
        col = get_col(remaining_code, 0, 7)
        # check if the id is higher than current highest
        if seat_id(row, col) > highest_id:
            highest_id = seat_id(row, col)
    return highest_id


# part 2 driver code
def part_2(seat_codes: list) -> int:
    # create empty dictionary with row number as key and cols as values
    seats = {}

    for seat in seat_codes:
        # get row and column from seat code
        row, remaining_code = get_row(seat, 0, 127)
        col = get_col(remaining_code, 0, 7)
        # check if row number is in dictionary's key's
        if row not in seats.keys():
            seats[row] = []
        # append column number to row's dictionary value
        seats[row].append(col)

    # find the row number with the empty column
    row, seat_list = non_full_row(seats)
    # find the missing seat number
    seat = missing_seat(seat_list)
    # return the seat id for missing seat (your seat id)
    return seat_id(row, seat)


# driver code
if __name__ == "__main__":
    # get seat codes as a list
    seat_codes = handle_input()

    # outputs
    print("Part 1:", part_1(seat_codes))
    print("Part 2:", part_2(seat_codes))
