class teste_eq_segundo_grau2:
    def teste_eq_segundo_grau3():
        from math import sqrt
        a = int(input("Digite o valor de A: "))
        b = int(input("Digite o valor de B: "))
        c = int(input("Digite o valor de C: "))
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Delta negativo")
        else:
            raiz_delta = sqrt(delta)
        x1 = (-b + raiz_delta)/2*a
        x2 = (-b - raiz_delta)/2*a
        print("As raízes são", x1, "e", x2)