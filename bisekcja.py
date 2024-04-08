import sympy

xp = -2
xk = 2
eps = 0.001

x = sympy.Symbol('x')
def funkcja(x):
    return sympy.sin(pow(x, 2) - x + 1/3) + 5*x/2

def pierwiastek(xp, xk, eps):
    x0 = (xp + xk)/2
    f0 = funkcja(x0)
    fp = funkcja(xp)
    if (abs(f0)<eps):
        print("Znaleziono pierwiastek rownania ktory wynosi x0 = ", x0)
    else:
        if (f0*fp < 0):
            xk = x0
            return pierwiastek(xp, xk, eps)
        else:
            xp = x0
            return pierwiastek(xp, xk, eps)


pierwiastek(-2, 2, 0.001)

