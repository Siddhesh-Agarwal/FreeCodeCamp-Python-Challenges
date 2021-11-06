def arithmetic_arranger(problems, show_results=False):
    # raise error if more than 5 problems are given
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = [""] * 4 if show_results else [""] * 3
    for problem in problems:
        num1, operator, num2 = problem.split() # split problem into 3 parts - operator and 2 numbers
        
        # ERRORS
        # raise error if problem is not addition or subtraction
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        # raise error if value is not a number
        elif not (num1.isnumeric() and num2.isnumeric()):
            return "Error: Numbers must only contain digits."
        # raise error if number has more than 4 digits
        elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        size = 2 + len(str(max(int(num1), int(num2)))) # width of the problem
        arranged_problems[0] += " " * (size - len(num1)) + num1 + "    "
        arranged_problems[1] += operator + " " * (size - len(num2) - 1) + num2 + "    "
        arranged_problems[2] += "-" * (size) + "    "
        if show_results:
            result = str(eval(problem))
            arranged_problems[3] += " " * (size - len(result)) + result + "    "

    return str('\n'.join(arranged_problems))