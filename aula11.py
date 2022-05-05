# -- informando erros com try e except

lista = [1,10]
try:
    divisao = 10/1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0, euem!')
except IndexError:
    print('Erro ao acessar um Index inválido da lista, linha 6')
except Exception as ex:
    print('erro desconhecido. erro: {}'.format(ex))