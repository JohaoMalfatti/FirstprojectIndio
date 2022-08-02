class meu_dicionario2:
    def meu_dicionario3():
        meu_dicionario = {"A" : "casa" , "B":"carro" ,"C": "bola" , "D": "cachorro" ,"D" :  "mulher" }
        print(meu_dicionario)
        for chave in meu_dicionario:
            print(chave)#chave do dicionario
            print(chave+"-"+meu_dicionario[chave])#palavra mais a chave
        for i in meu_dicionario.items():
            print(i)
        
        for a in meu_dicionario.keys():
            print(a)