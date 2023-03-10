# type puzzle = [[string, int], [int, int][]][]
#               [[operand, total], [row, col][]][]

from sys import stdin

def extract_puzzle(puzzle_string):
    puzzle = []

    # Split the puzzle into individual cells and remove the first line
    cell_string_array = puzzle_string.replace(',', '\n').splitlines()[1:]

    print(cell_string_array)

def get_puzzle_array():
    raw_string = stdin.read()

    puzzle = extract_puzzle(raw_string)
