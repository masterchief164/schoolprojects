inp = input()


class FormulaError(Exception):
    pass


while inp != "quit":
    inp = inp.split()
    try:
        if len(inp) != 3:
            raise FormulaError
    except FormulaError:
        print('Input has less or more than 3 elements.')
    else:
        try:
            inp[0] = float(inp[0])
            inp[2] = float(inp[2])
        except ValueError:
            print('First and Third element must be an integer or float value.')
        else:
            try:
                val = ['+', '-', '*', '/']
                if inp[1] not in val:
                    raise FormulaError
            except FormulaError:
                print('Invalid operator.')
            else:
                if inp[1] == '+':
                    print(inp[0] + inp[2])
                elif inp[1] == '-':
                    print(inp[0] - inp[2])
                elif inp[1] == '*':
                    print(inp[0] * inp[2])
                elif inp[1] == '/':
                    print(inp[0] / inp[2])
    inp = input()
