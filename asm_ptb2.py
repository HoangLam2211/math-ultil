
from sympy import symbols, Eq, solve

try:

    with open('input.txt', 'r', encoding='utf8') as file:
        line_count = 0
        for line in file:
            solutions = []
            line_count += 1
            list_number = line.split()
            a = int(list_number[0])
            b = int(list_number[1])
            c = int(list_number[2])

            x = symbols('x')
            equation = Eq(a * x ** 2 + b * x + c, 0)
            equation_solutions = solve(equation, x)
            solutions.extend(equation_solutions)

            with open('output.txt', 'a', encoding='utf8') as outfile:
                outfile.write(f'equation : {line_count}\n')
                outfile.write(f'a = {a}, b = {b}, c = {c}\n')
                outfile.write(', '.join(map(str, solutions))+'\n')
        print('Solutions have been written to output.txt.')

except FileNotFoundError:
    print("Error: Input file 'input.txt' not found.")
except PermissionError:
    print("Error: Permission denied to access files.")
except ValueError as ve:
    print(f"Error in input file format: {ve}")
except Exception as e:
    print(f"Error: {e}")
