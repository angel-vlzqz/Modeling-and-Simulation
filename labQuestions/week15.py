import numpy as np

def trapezoidal_rule(f, a, b, n):
    """
    Numerically integrate the function f from a to b using the trapezoidal rule with n subdivisions.
    """
    h = (b - a) / n
    integral = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Test functions
def polynomial(x):
    return x**2

def trigonometric(x):
    return np.sin(x)

# Parameters for integration
a = 0  # lower bound
b = 1  # upper bound for polynomial
c = np.pi  # upper bound for trigonometric
n = 1000  # number of subdivisions

# Calculate integrals
integral_poly = trapezoidal_rule(polynomial, a, b, n)
integral_trig = trapezoidal_rule(trigonometric, a, c, n)

print(f"The integral of x^2 from {a} to {b} is approximately {integral_poly:.4f}")
print(f"The integral of sin(x) from {a} to {c} (pi) is approximately {integral_trig:.4f}")

