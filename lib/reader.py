# type puzzle = [[string, int], [int, int][]][]
#               [[operand, total], [row, col][]][]

from sys import stdin
from re import compile

KENKEN_REGEX = compile(r"^#kenken.*")

def get_input():
    inp = stdin.read()
    cleaned = inp.strip().replace(',', '\n')

    line_split = cleaned.splitlines()

    # We don't want empty strings or the starting comment line
    return [
        line
        for line in line_split
        if (line != "" and KENKEN_REGEX.match(line) is None)
    ]

def get_operand_total(op_str):
    operand = op_str.lstrip("0123456789")
    total = int(op_str.rstrip("+-*/"))

    return (operand, total)

# Helper function to convert an index to an associated row and column
def get_row_col(num):
    row = num // 7
    col = num % 7

    return (row, col)

def get_operator_block(cell):
    cell = cell.lstrip("r")
    cell = cell.split(".")

    block_num = int(cell[0]) - 1

    if len(cell) == 1:
        return (block_num, None)
    else:
        return (block_num, cell[1])

def extract_puzzle(cell_string_array):
    puzzle = []

    # Error conditions that we should never hit
    if len(cell_string_array) == 0:
        print("No cells found")
        exit(1)
    elif len(cell_string_array) > 49:
        print("Too many cells")
        exit(1)

    for i in range(49):
        row, col = get_row_col(i)

        block, operator = get_operator_block(cell_string_array[i])

        if block >= len(puzzle):
            puzzle.append((None, []))

        puzzle[block][1].append((row, col))

        if operator is not None:
            operand_tup = get_operand_total(operator)
            coords_list = puzzle[block][1]
            puzzle[block] = (operand_tup, coords_list)

    return puzzle

def get_puzzle_array():
    cell_string_array = get_input()

    return extract_puzzle(cell_string_array)
