# ----- Lambda ------
#Forma de simplicar algo descrito no código
#simplificação do contador

contador_letras = lambda lista: [len(x) for x in lista]
#função anonima

lista_animais = ['cachorro', 'gato', 'elefante']
contador_letras(lista_animais)
print(contador_letras(lista_animais))

soma = lambda a,b: a+b
sub = lambda a,b: a-b
print(soma(5,10))
print(sub(10,5))

calculadora = {
    'soma':lambda a,b: a+b,
    'subtração': lambda a,b: a-b,
    'multiplicação': lambda a,b: a*b,
    'divisão': lambda a,b: a/b,
}
print(type(calculadora))
soma = calculadora['soma']
sub = calculadora ['subtração']
multiplicacao = calculadora ['multiplicação']
div = calculadora ['divisão']

print(soma(10,5))
print(sub(10,8))
print(multiplicacao(10,2))
print(div(5,2))
