# lista = [12, 10, 7, 5]
# lista_animal = ['cachorro', 'gato', 'elefante', 'lobo','arara']

# print(lista_animal[1])

# # ---- ordenar listas de registros -------
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)

# ----- ordenação reversa de valores com .reverse -----
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# -------- Soma normal ---------
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# # -------- Soma com [sum] ----------
# print(sum(lista))

#  --------- pegar maior valor da lista --------
# print(max(lista_animal))

# ---------- pegar menor valor da lista [ordem alfabetica] --------
# print(min(lista_animal))


# ------- Se existe um elemento procurado na lista ex: gato -------
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um gato na lista')

# --------- multiplicar lista ---------
#
# nova_lista = lista_animal * 3
# print(nova_lista)
#
# if 'lobo' in lista_animal:
#      print('existe um lobo na lista')
# else:
#      print('não existe um lobo na lista')


# ------ incluir novos registros a lista com .append ex: lobo -------
# if 'lobo' in lista_animal:
#      print('existe um lobo na lista')
# else:
#      print('se não existe um lobo na lista, ele sera incluido')
#      lista_animal.append('lobo')
#      print(lista_animal)

# ----- retirar registro da lista, retirando o valor 'gato' --------
# lista_animal.pop(2)
# print(lista_animal)

# ----- retirar registro da lista com .remove -----
# lista_animal.remove('elefante')
# print(lista_animal)



# ------ TUPLA ---------
# lista = [12, 10, 7, 5]
# lista_animal = ['cachorro', 'gato', 'elefante', 'lobo','arara']

#A tupla  é imutavel
# a lista é mutavel, conseguimos alterar os valores e editar
#
# tupla = (1,10,12,14)
# print(tupla[0])

# ---- contador com tupla ------
# tupla = (1,10,12,14)
# print(len(tupla))

# resposta = 4

# ----- conversão de lista para tupla -----
# lista = [12, 10, 7, 5]
# lista_animal = ['cachorro', 'gato', 'elefante', 'lobo','arara']
#
# tupla = (1,10,12,14)
# print(len(tupla))
# print(len(lista_animal))
# tupla_animal = tuple (lista_animal)
# print(type(tupla_animal))
# print(tupla_animal)
#
# # ----- conversão de tupla para lista -----
# lista_numerica = list(tupla)
# print(type(lista_numerica))
# lista_numerica[0] = 100
# print(lista_numerica)



