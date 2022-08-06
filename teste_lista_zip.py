class teste_lista_zip2:
    def teste_lista_zip3():
        
        lista1 = [1,2,3,4,5]
        lista2 = ["Opala", "Mustang","Chvette","Dodge","Vectra"]
        lista3 = ["GM", "fORD","GM","Dodge","Opel"]
        
        for numero, modelo, marca in zip(lista1, lista2, lista3):
            print(numero, modelo,marca)
            