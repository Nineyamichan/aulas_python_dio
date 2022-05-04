
# --- classe

class Calculadora:
# ----- Funcao ------
#Metodo: não retorna valor
#Funcao: tudo que retorna valor
# declaracao de definição = def
    def __init__(self, num1,num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a+self.valor_b

    def subtracao(self):
        return self.valor_a-self.valor_b

    def multiplic(self):
        return self.valor_a*self.valor_b

    def divi(self):
        return self.valor_a/self.valor_b

    #instancia de classe
if __name__ == '__main__':
    calculadora = Calculadora(5,10)
    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divi())
    print(calculadora.multiplic())

