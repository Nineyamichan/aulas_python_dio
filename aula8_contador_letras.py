# -- metodo que conta palavras

contador = []
def contador_letras (lista_letras):
    for x in lista_letras:
        quant = len(x)
        contador.append(quant)
    return contador

def teste ():
    return 'teste'
if __name__ == '__main__':
    list = ['cachorro', 'gato']
    print(contador_letras(list))
