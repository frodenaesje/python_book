# file: ex_07_07_equation_quiz_start.py
import random

students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

def generate_equation():
    """Generate a random linear equation ax + b = cx + d.
    Returns (equation_string, solution) where solution is an integer.
    Guarantees a != c (solvable) and integer solution.
    """
    while True:
        a = random.randint(-9, 9)
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)
        d = random.randint(-9, 9)
        if a == c:
            continue
        if (d - b) % (a - c) != 0:
            continue
        solution = (d - b) // (a - c)

        def coeff(n):
            if n == 1: return 'x'
            if n == -1: return '-x'
            return f'{n}x'

        def const(n, first=False):
            if first: return str(n)
            if n >= 0: return f'+ {n}'
            return f'- {-n}'

        lhs = f"{coeff(a)} {const(b, first=False)}" if b != 0 else coeff(a)
        rhs = f"{coeff(c)} {const(d, first=False)}" if d != 0 else coeff(c)
        eq = f"{lhs} = {rhs}"
        return eq, solution


# TODO: Build the quiz dict
#       For each student, generate 4 equations and store in nested dict:
#       quiz[name] = {
#           'equations': [...],
#           'solutions': [...],
#           'answers':   []
#       }

# TODO: Ask the user for a student name
#       Validate that the name is in the quiz dict

# TODO: For each equation:
#       - Print the equation
#       - Read and store the student's integer answer in 'answers'

# TODO: Print results
#       For each equation show: equation, correct answer, student answer, OK/Wrong
#       Print total correct out of 4
