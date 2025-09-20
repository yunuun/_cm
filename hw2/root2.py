import cmath

def root2(a, b, c):
    d = b**2 - 4*a*c
    ans1 = (-b + (cmath.sqrt(d)))/(2*a)
    ans2 = (-b - (cmath.sqrt(d)))/(2*a)
    def f(x):
        return a*(x**2) + b*x +c
    return ans1, cmath.isclose(f(ans1), 0), ans2, cmath.isclose(0, f(ans2))

print(root2(1, -5, 6))
