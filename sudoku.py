import sys


# check and eliminate possible numbers in a given column
def row_control(row_number, sudoku_map, possible_num_list):
    for column in range(9):
        checked_num = sudoku_map[row_number][column]
        if checked_num > 0:
            if checked_num in possible_num_list:
                possible_num_list.remove(checked_num)


# check and eliminate possible numbers in a given row
def column_control(column_number, sudoku_map, possible_num_list):
    for row in range(9):
        checked_num = sudoku_map[row][column_number]
        if checked_num > 0:
            if checked_num in possible_num_list:
                possible_num_list.remove(checked_num)


# check and eliminate possible numbers in a 3x3 square
def square_control(row_number, column_number, sudoku_map, possible_num_list):

    # first row of 3x3 squares
    if 0 <= row_number <= 2:
        # northwest square
        if 0 <= column_number <= 2:
            for row in range(0, 3):
                for column in range(0, 3):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)
        # north square
        elif 3 <= column_number <= 5:
            for row in range(0, 3):
                for column in range(3, 6):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)
        # northeast square
        elif 6 <= column_number <= 8:
            for row in range(0, 3):
                for column in range(6, 9):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)

    # second row of 3x3 squares
    if 3 <= row_number <= 5:
        # west square
        if 0 <= column_number <= 2:
            for row in range(3, 6):
                for column in range(0, 3):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)

        # center square
        elif 3 <= column_number <= 5:
            for row in range(3, 6):
                for column in range(3, 6):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)

        # east square
        elif 6 <= column_number <= 8:
            for row in range(3, 6):
                for column in range(6, 9):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)

    # third row of 3x3 squares
    if 6 <= row_number <= 8:
        # southwest square
        if 0 <= column_number <= 2:
            for row in range(6, 9):
                for column in range(0, 3):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)

        # south square
        elif 3 <= column_number <= 5:
            for row in range(6, 9):
                for column in range(3, 6):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)

        # southeast square
        elif 6 <= column_number <= 8:
            for row in range(6, 9):
                for column in range(6, 9):
                    checked_num = sudoku_map[row][column]
                    if checked_num > 0:
                        if checked_num in possible_num_list:
                            possible_num_list.remove(checked_num)


def solve(step, output_file, sudoku_map):
    possible_num_list = [numbers for numbers in range(1, 10)]
    for _ in range(18):
        output_file.write("-")
    for row_number in range(9):
        for column_number in range(9):
            if sudoku_map[row_number][column_number] == 0:
                row_control(row_number, sudoku_map, possible_num_list)
                column_control(column_number, sudoku_map, possible_num_list)
                square_control(row_number, column_number, sudoku_map, possible_num_list)
                if len(possible_num_list) == 1:
                    # if there is only one possible number fill in the cell and print the step
                    sudoku_map[row_number][column_number] = possible_num_list[0]
                    output_file.write("\nStep {} - {} @ R{}C{}\n".format(step, possible_num_list[0], row_number + 1, column_number + 1))
                    for _ in range(18):
                        output_file.write("-")
                    output_file.write("\n")
                    for row_write in range(9):
                        for column_write in range(9):
                            output_file.write(str(sudoku_map[row_write][column_write]) + " ")
                        output_file.write("\n")
                    step = step + 1
                    solve(step, output_file, sudoku_map)
                possible_num_list = [numbers for numbers in range(1, 10)]


def main():

    input = sys.argv[1]
    output = sys.argv[2]

    input_file = open(input, "r")
    sudoku_map = [[int(numbers) for numbers in line.split()] for line in input_file]
    output_file = open(output, "w")

    solve(1, output_file, sudoku_map)

    input_file.close()
    output_file.flush()
    output_file.close()


if __name__ == "__main__":
    main()
