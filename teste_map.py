from operator import xor
class teste_map2:
    def teste_map3(x):
        return x*2
    valor = [1,2,3,4,5,6,7,8,9]
    dobro_valor = map(teste_map3, valor)
    dobro_valor = list(dobro_valor)
    print(dobro_valor)
    #função map altera o valor todo da lista