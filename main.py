import sympy as sp

def main():
    print("Que voulez-vous faire ? :")
    a = [second_degre(), oui()]
    a[1]

def oui():
    print("salut")

def second_degre():

    # Définir les variables
    x = sp.symbols('x')

    # Définir les coefficients de l'équation du second degré
    a = 1
    b = 2
    c = 5

    # Définir l'équation
    equation = a*x**2 + b*x + c

    # Résoudre l'équation
    solutions = sp.solve(equation, x)

    print("Les solutions de l'équation sont :", solutions)



main()