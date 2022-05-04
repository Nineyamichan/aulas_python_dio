# # ------ conjuntos -------
# conjunto = {1,2,3,4}
# print(type(conjunto))
#
# print(conjunto)
# #não permite duplicidade
#
#
# # ----- Adicionar ao conjunto com .add -----
# conjunto.add(5)
# print(conjunto)
#
# # ----- Remover elementos com   -------
# conjunto.discard(2)
# print(conjunto)


# ----- união de dois conjuntos ------
# conjunto = {1,2,3,4,5}
# conjunto2 = {5,6,7,8}
#
# conjunto_uniao =  conjunto.union(conjunto2)
# print('União: {}'.format(conjunto_uniao))

# ----- interssecção de conjuntos  -----
# conjunto = {1,2,3,4,5}
# conjunto2 = {5,6,7,8}

# conjunto_intersec = conjunto.intersection(conjunto2)
# print('intersecção: {}'.format(conjunto_intersec))
# resultado: 5

# ----- Diferença entre conjuntos  -----
# conjunto = {1,2,3,4,5}
# conjunto2 = {5,6,7,8}
#
# conjunto_difenca = conjunto.difference(conjunto2)
# print(conjunto_difenca)


# ----- Diferença simetrica  -----
# conjunto = {1,2,3,4,5}
# conjunto2 = {5,6,7,8}
#
# conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
# print('Diferença simetirca {}'.format(conjunto_diff_simetrica))
#
# Resultado: {1, 2, 3, 4, 6, 7, 8} somente o 5 tem em ambos conjuntos comparativos

# ----- Função subset  -----
# conjunto_a = {1,2,3}
# conjunto_b = {1,2,3,4,5}
#
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print('A é subconjunto de B: {}'.format(conjunto_subset))

# resultado: true, porque o que possui no conjunto a também possui no conjunto b

# --- conjunto superset ------
# conjunto_a = {1,2,3}
# conjunto_b = {1,2,3,4,5}
#
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print('B é superconjunto de A: {}'.format(conjunto_superset))
#
# resultado: true, porque o conjunto B é um super conjunto do conjunto A
# Sempre que um conjunto for subset de outro, o outro é superset do outro conjunto

# ------ converter uma lista para conjuntos ----
#retirar duplicidade
#
# lista = {'cachorro', 'cachorro', 'gato', 'gato', 'elefante'}
# conjunto_animais = set(lista)
# print(conjunto_animais)
#
# resultado: {'gato', 'elefante', 'cachorro'}

# # ------ converter conjuntos de volta para a lista ------
# lista = {'cachorro', 'cachorro', 'gato', 'gato', 'elefante'}
# print(lista)
# conjunto_animais = set(lista)
# print(conjunto_animais)
#
# lista_animais = list(conjunto_animais)
# print(lista_animais)

