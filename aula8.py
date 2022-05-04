# ---- Interação de módulos - TV

from aula7parte3_TV import Television
from aula7 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    television = Television()
    print(television.ligada)
    television.power()
    print(television.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    list = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(list)
    print('total de letras por palavra da lista: {}'.format(total_letras))
    print(teste())
