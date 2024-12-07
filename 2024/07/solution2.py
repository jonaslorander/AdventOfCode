import itertools

equations = open("input.txt").read().splitlines()

def find_operators(equation):
    res = int(equation.split(": ")[0])
    terms = equation.split(": ")[1].split(" ")

    # Create table with all possible combinations 
    #  Max number of combinations are 2^(n - 1)
    #  where n is the number of terms in an equation
    operators = itertools.product(['*','+', '|'], repeat=(len(terms) - 1))
    # Convert tuples to list
    operators = [list(c) for c in operators]

    # Test all possible combinations
    for o in operators:
        eval_res = int(terms[0])
        for o, t in zip(o, terms[1:]):
            if o == '*':
                eval_res *= int(t)
            elif o == '+':
                eval_res += int(t)
            elif o == '|':
                eval_res = int(str(eval_res) + str(t))

        # Leave function if we find one that is true
        if eval_res == res:
            return res

    return None

calibration_result = 0

for e in equations:
    result = find_operators(e)
    if result:
        calibration_result += result

print(calibration_result)