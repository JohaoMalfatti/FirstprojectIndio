from this import d


class teste_lista_comprehension2:
    def teste_lista_comprehension3():
        x = [1,2,3,4,5]
        y=[i**2  for i in x]#numero ao quadrado
        z=[i for i in x if i%2==1] #vai trazer somente os numeros impares
        print("List comprehension")
        print(x)
        print(y)
        print(z)
        