from tkinter import W


class teste_arquivos2:
    def teste_arquivos3():
        w = open("arquivo2.txt","w")   
        w.write("Esse é o meu arquivo\n")
        w.write("Esse guardanapo amassado diz como é que eu to\n" "sofrendo por amor, sofrendo por amor")
        w.close()
        
        arquivo = open("arquivo2.txt","r")
        print(arquivo.readline())
        
        texto_completo = arquivo.read()
        print(texto_completo)