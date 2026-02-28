def arithmetic_arranger(problems, show_answers=False):
    # 1. Check if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        # 2. Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # 3. Validate digits
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        # 4. Validate length
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate width of the column
        length = max(len(num1), len(num2)) + 2
        
        # Build the individual components for this problem
        top = num1.rjust(length)
        bottom = operator + num2.rjust(length - 1)
        line = "-" * length
        
        first_line.append(top)
        second_line.append(bottom)
        dashes.append(line)

        if show_answers:
            res = str(eval(problem))
            answers.append(res.rjust(length))

    # 5. Join all parts with 4 spaces
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes)
    )

    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems