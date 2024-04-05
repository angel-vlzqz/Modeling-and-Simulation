import sympy as sp
from sympy import solve

def taylor_expansion(f, x0, n):
    x = sp.symbols('x')
    taylor = f.subs(x, x0)
    for i in range(1, n+1):
        derivative = f.diff(x, i)
        taylor += (derivative.subs(x, x0) / sp.factorial(i)) * (x - x0)**i
    return taylor

def solve_differential_equation(f, x, y, x0, y0, y_prime0, n):
    equation = f.subs([(x, x0), (y, y0), (y.diff(x), y_prime0)])
    for i in range(1, n+1):
        derivative = f.diff(y, i)
        equation += (derivative.subs([(x, x0), (y, y0), (y.diff(x), y_prime0)])) / sp.factorial(i) * (x - x0)**i
    return solve(equation, y)

# Part 1(a)
x = sp.symbols('x')
y = sp.Function('y')(x)
f = y.diff(x, 2) - 2 * x * y.diff(x) + x**2 * y
x0 = 0
y0 = 1
y_prime0 = -1
n = 4

taylor = taylor_expansion(f, x0, n)
solution = solve_differential_equation(f, x, y, x0, y0, y_prime0, n)

print("Taylor expansion:")
print(taylor)
print("Solution at x = 3.5:")
print(solution.subs(x, 3.5))
