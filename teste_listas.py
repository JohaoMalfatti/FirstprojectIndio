class teste_listas2:
    def teste_litas3():
        minha_lista = ["Opala", "Camaro","Mustang"]
        minha_lista2 = [1,2,3]
        minha_lista3 = [4100, 3,199, 5.0]
        minha_lista4 = ["Primeiro", False, True]
        minha_lista5 = [1,3,5,6,7]
        
        for item in minha_lista:
            print(item) #percore itens na lista
        
        tamanho = len(minha_lista)
        print(tamanho) #mostra o tamanho da lista
        
        minha_lista.append("Silverado") #adiciona itens a lista
        if "Opala" in minha_lista:
            print("Opala melhor carro da lista") #exibe valores na lista
        del minha_lista[1]
        print(minha_lista)#deleta o item selecionado    
        
        minha_lista2.sort()
        print(minha_lista2)#ordena a lista ja existente
        
        minha_lista4.reverse()
        print(minha_lista4)#reverte a lista
        
        minha_lista5.sorted(minha_lista3)
        print(minha_lista5)#ordena a lista sem alterar
        
        