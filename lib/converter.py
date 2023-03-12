#!/usr/bin/env python3
# type puzzle = [[string, int], [int, int][]][]
#               [[operand, total], [row, col][]][]

def smt_converter(puzzle):
    solver_input = "(set-logic UFNIA)\n"
    solver_input += "(set-option :produce-models true)\n"
    solver_input += "(set-option :produce-assignments true)\n"
    # declare the variables V0, ..., V48
    for i in range(49):
        variable = "V" + str(i)
        declare_const = "(declare-const " + variable + " Int)\n"
        solver_input += declare_const

    # set the range for each varaiable
    for i in range(49):
        variable = "V" + str(i)
        set_range = "(assert (and (> " + variable + " 0) (< " + variable + " 10)))\n"
        solver_input += set_range

    # constraints that variables have to be unique on each row
    for i in range (7):
        row_unique = "(assert (distinct"
        for j in range(7*i, 7*i+7):
             row_unique += " V" + str(j)
        row_unique += " ))\n"
        solver_input += row_unique

    # constraints that variables have to be unique on each column
    for i in range(7):
        col_unique = "(assert (distinct"
        for j in range(i, 49, 7):
            col_unique += " V" + str(j)
        col_unique += " ))\n"
        solver_input += col_unique

    # constraints from the puzzle
    # type puzzle = [[string, int], [int, int][]][]
    #               [[operand, total], [row, col][]][]
    for tuple in puzzle:
        total = str(tuple[0][1]) # str
        operand = tuple[0][0] # str
        var_num_list = [] # str[]
        for coord in tuple[1]:
            row = coord[0]
            col = coord[1]
            var_num = row*7 + col
            var_num_list.append('V' + str(var_num))

        operand_const = "(assert ("

        if (operand == ''):
            operand_const += "= " + total + " ("
            for num_str in var_num_list:
                 operand_const += num_str
            operand_const += ")))\n"
            solver_input += operand_const

        elif (operand == '+' or operand == '*'):
            operand_const += "= " + total + " (" + operand
            for num_str in var_num_list:
                operand_const += " " + num_str
            operand_const += ")))\n"
            solver_input += operand_const

        else:
            operand_const += "or (= " + total + " (" + operand
            for num_str in var_num_list:
                operand_const += " " + num_str
            operand_const += "))"
            reverse = var_num_list[::-1]
            operand_const += "(= " + total + " (" + operand
            for num_str in reverse:
                operand_const += " " + num_str
            operand_const += "))))\n"
            solver_input += operand_const

    return solver_input
