from msilib.schema import Class


var_1 = 10
var_2 = 8
soma = var_1+var_2
 


var_3 = "johao"
var_4 = "malfatti"

print(str(soma) + var_3 + var_4)

######################################################
class calc:

    def Somar(var1, var2): 
        return print(var1 + var2)  

    
    def Subtrair(var1, var2): 
        return print(var1 - var2)  


    def Multiplicar(var1, var2): 
        return print(var1 * var2)  


    def Dividir(var1, var2): 
         return print(var1 / var2)  

calc.Somar(4,5)
calc.Subtrair(4,2)
calc.Multiplicar(3,3)
calc.Dividir(4,2)
