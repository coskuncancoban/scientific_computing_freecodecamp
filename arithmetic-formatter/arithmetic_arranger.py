def arithmetic_arranger(problems, result=False):

    #check the problems are more than five.
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    line = ""
    results = ""

    #seperate the problems.
    for problem in problems:

        #seperate the piece of problem.
        a = problem.split(" ")[0]
        sign = problem.split(" ")[1]
        b = problem.split(" ")[2]

        #check the sign is "+" or "-".
        if sign not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        #check the numbers are digit.
        if not (a.isdigit and b.isdigit()):
            return "Error: Numbers must only contain digits."

        #check the numbers are more than four digits.
        if len((str(max(a, b)))) > 4:
            return "Error: Numbers cannot be more than four digits."

        #lenght of a quest
        if int(a) > int(b):
            lenght = len(a) + 2
        else:
            lenght = len(b) + 2

        #construct first line
        first_line = first_line + a.rjust(lenght) + "    "

        #constract second line with operation sign
        second_line = second_line + sign + b.rjust(lenght - 1) + "    "

        #construct operation line
        line = line + (lenght * "-") + "    "

        #find the results and constract the line of results
        if result:
            if sign == "+":
                results = results + f"{str(int(a) + int(b)).rjust(lenght)}" + "    "
            else:
                results = results + f"{str(int(a) - int(b)).rjust(lenght)}" + "    "

    #remove unwanted spaces from end of the lines
    first_line = first_line[:-4]
    second_line = second_line[:-4]
    line = line[:-4]
    results = results[:-4]

    #construct the outcome
    if result:
        return (f"{first_line}\n{second_line}\n{line}\n{results}")
    else:
        return (f"{first_line}\n{second_line}\n{line}")
