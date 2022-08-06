from functools import reduce

class teste_reduce2:
    def soma(x, y):
            return x+y
    lista = [1,2,3,4,5]
    soma = reduce(soma,lista)
    print(soma)