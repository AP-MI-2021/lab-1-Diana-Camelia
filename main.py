"""
1. [2.5p] Să se stabilească daca un număr n este prim sau nu. Exemplu: n = 3 este prim, dar n = 6 nu este prim.
2. [2.5p] Să se calculeze produsul a n numere naturale Exemplu: n = 3 și numerele 3, 4, 5, produsul este 60.
3. [5p] Să se calculeze CMMDC a 2 numere folosind doi algoritmi distincți.
"""

def is_prime():
    """
    Determina daca un numar dat este prim sau nu.
    :param n: (x) un numar intreg.
    :return: True, daca numarul este prim, respectiv False in caz contrar.
    """
    n = int(input("Dati un numar: "))
    ok = True
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0 and ok == True:
            ok = False
    if ok:
        return True
    else:
        return False

def citire_lista(lst):
    """
    Citeste o lista cu n elemente date de la tastutura.
    :param lst: O lista de numere intregi.
    :return: Lista.
    """
    # solicităm numărul de elemente
    n = int(input("Dati numarul de elemente: "))
    for x in range(n):
        lst.append(int(input("Element: ")))
    return lst

def produsul_a_n_nr(lst):
    """
    Calculeaza produsul elementelor din lista.
    :param lst: Lista de numere intregi.
    :return: Produsul elementelor din lista.
    """
    p = 1
    x = len(lst)
    for i in range(x):
        p = p * lst[i]
    return p

def test_produsul_a_n_nr():
    assert produsul_a_n_nr([2,3,1]) == 6
    assert produsul_a_n_nr([1,1,3,2,2]) == 12
    assert produsul_a_n_nr([1,10,99,0]) == 0
    assert produsul_a_n_nr([3,4,5]) == 60

def CMMDC1():
    """
    Calculeaza cel mai mare divizor comun a doua numere introduse de la tastatura (METODA 1).
    param a: Primul numar intreg.
    param b: Al doilea numar intreg.
    :return: Cel mai mare divizor comun al celor doua numere.
    """
    print("Prima pereche de doua numere intregi: ")
    a = int(input("Dati primul numar intreg: "))
    b = int(input("Dati al doilea numar intreg: "))
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    k = a
    return k

def CMMDC2():
    """
    Calculeaza cel mai mare divizor comun a doua numere introduse de la tastatura (METODA 2).
    param c: Primul numar intreg.
    param d: Al doilea numar intreg.
    :return: Cel mai mare divizor comun al celor doua numere.
    """
    print("A doua pereche de doua numere intregi: ")
    c = int(input("Dati primul numar intreg: "))
    d = int(input("Dati al doilea numar intreg: "))
    rest = c % d
    e = 0
    while rest != 0:
        c = d
        d = rest
        rest = c % d
        e = d
    return e

while True:
    lst = []
    test_produsul_a_n_nr()
    a = is_prime()
    print(a)
    citire_lista(lst)
    print(produsul_a_n_nr(lst))
    print(CMMDC1())
    print(CMMDC2())
    break