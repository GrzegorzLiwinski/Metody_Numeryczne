import numpy
import matplotlib as pyplot
import sympy
import scipy.misc


x = sympy.Symbol('x')
def funkcja(x):
  return sympy.sin(pow(x, 2) - x + 1/3) + 5*x/2

def pierwszaPochodna(x):
  f_x = funkcja(x)
  wynik = f_x.diff(x)
  print("Pierwsza pochodna wynosi: ", wynik)
  return wynik

def wynikPochodnej1(x):
  return (2*x - 1)*sympy.cos(x**2 - x + 1/3) + 5/2


def drugaPochodna(x):
  drugaPochodna = pierwszaPochodna(x).diff(x)
  print("Druga pochodna wynosi: ", drugaPochodna)
  return drugaPochodna

def wynikPochodnej2(x):
  return -(2*x - 1)**2*sympy.sin(x**2 - x + 0.333333333333333) + 2*sympy.cos(x**2 - x + 0.333333333333333)

print(drugaPochodna(x))

print("")
print("Wartosc funkcji dla x=2 wynosi: ", funkcja(2))
print("Pochodna dla x=2 wynosi: ", wynikPochodnej1(2))
print("Druga pochodna dla x=2 wynosi: ", wynikPochodnej2(2))
print("")
print("Wartosc funkcji dla x=-2 wynosi: ", funkcja(-2))
print("Pochodna dla x=-2 wynosi: ", wynikPochodnej1(-2))
print("Druga pochodna dla x=-2 wynosi: ", wynikPochodnej2(-2))
print("")
print("Wartosc funkcji dla x=-1 wynosi: ", funkcja(-1))
print("Pochodna dla x=-1 wynosi: ", wynikPochodnej1(-1))
print("Druga pochodna dla x=-1 wynosi: ", wynikPochodnej2(-1))
print("")
print("Wartosc funkcji dla x=0 wynosi: ", funkcja(0))
print("Pochodna dla x=0 wynosi: ", wynikPochodnej1(0))
print("Druga pochodna dla x=0 wynosi: ", wynikPochodnej2(0))

print("Wybieramy przedział [-1,0], w ktorym szukamy rozwiazania. Funkcja i druga pochodna maja ten sam znak, wiec spelniaja zalozenia ")
x0 = 0
print("xo wynosi: ", x0)
x1 = x0 - (funkcja(0)/wynikPochodnej1(0))
print("x1 wynosi: ", x1)
x2 = x1 - (funkcja(x1)/wynikPochodnej1(x1))
print("x2 wynosi: ", x2)
x3 = x2 - (funkcja(x2)/wynikPochodnej1(x2))
print("x3 wynosi: ", x3)
x4 = x3 - (funkcja(x3)/wynikPochodnej1(x3))

print("Mozemy wiec przyjac, ze przyblizonym pierwiastkiem rownania sin(pow(x, 2) - x + 1/3) + 5*x/2 jest wartosc: x=-0.232266973118682")

eps = 0.001
xp = -1
xk = 0
def metodaFalsi(xp, xk, eps):

  xi = xp - ((xk-xp)/(funkcja(xk)-funkcja(xp)))*funkcja(xp)
  # print(xi)
  if (funkcja(xi) == 0 or abs(xi) < eps):
    print("xi = ", xi, " jest szukanym pierwiastkiem metody siecznych")
    return xi
  else:
    if (funkcja(xp)*funkcja(xi) < 0):
      xk=xi
      return metodaFalsi(xp, xk, eps)
    else:
      xp = xi
      return metodaFalsi(xp, xk, eps)

metodaFalsi(xp, xk, eps)

