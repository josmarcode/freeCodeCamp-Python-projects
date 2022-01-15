def arithmetic_arranger(problems, op=False):

    arranged_problems = ''
    l0, l1, l2, l3 = '', '', '', ''
    count = 0
    for problem in problems:
        count += 1
        entrie = problem.split()

        # Input errors
        if len(problems) > 5:
            return "Error: Too many problems."

        try:
            int(entrie[0]), int(entrie[2])
        except:
            return "Error: Numbers must only contain digits."

        if len(entrie) != 3:
            return f'Excess or missing terms in the entry {count}.'

        if entrie[1] != '+' and entrie[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if len(entrie[0]) > 4 or len(entrie[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Size comparison
        a, b = int(entrie[0]), int(entrie[2])

        m = max([a, b])
        width = len(str(m)) + 2

        # Line's constructor
        l0 += ' ' * (width - len(entrie[0])) + f'{entrie[0]}'
        l1 += f'{entrie[1]}' + ' ' * \
            (width - 1 - len(entrie[2])) + f'{entrie[2]}'
        l2 += '-' * width
        if op:
            # Suma
            if entrie[1] == '+':
                r = a + b
                l3 += ' ' * (width - len(str(r))) + f'{r}'
            # Resta
            elif entrie[1] == '-':
                r = a - b
                l3 += ' ' * (width - len(str(r))) + f'{r}'

        # Space generator
        if count < len(problems):
            l0 += 4 * ' '
            l1 += 4 * ' '
            l2 += 4 * ' '
            if op:
                l3 += 4 * ' '

    arranged_problems += l0 + '\n' + l1 + '\n' + l2
    if op:
        arranged_problems += '\n' + l3

    return arranged_problems

# Input
c = int(input("How many operations will be made?\n"))
if c != 0:
    ops = []
    print("Write your operation as 'a + b' and press Enter")
    for _ in range(c):
        operation = input("Operation: ")
        ops.append(operation)
    print(arithmetic_arranger(ops, True))

