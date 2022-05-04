# --- comando FOR (Número primo) -----------------------------

#a = int(input("Entre com um número: "))

#for x in range (1, a+1):
#    resto = a % x
#    print(resto)

# --- Número primo - com if e for  -----------------------------
#a = int(input("Entre com um número: "))

#div = 0
#for x in range (1, a+1):
#    resto = a % x
#   print(x,resto)

#    if resto == 0:
#        div = div + 1

#if div == 2:
#    print("Número {} é primo".format(a))
#else:
#    print("Número {} não é primo".format(a))

# --- Todos os números primos  -------------------------------
#for num in range(101):
#    div = 0
#    for x in range (1, num+1):
#        resto = num % x
#       # print(x,resto)

#        if resto == 0:
#            div = div + 1

#    if div == 2:
#        print(num)

# ---- Todos os números primos com entrada de usuário  ---------------------

# a = int(input("entre com um valor:  "))
# for num in range(a+1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         if resto == 0:
#              div += 1
#
#     if div == 2:
#         print(num)
#

# ------- Laço de repetição While -------------------------

# a = 0
# while a <= 10: #Enquanto a for menor ou igual a 10
#     print(a)
#     a +=1


#nota = int (input('entre com uma nota'))
#while nota > 10:
#    nota = int(input('nota invalida, entre com uma nota correta'))


# ------------ Laço de repetição while para digitar a nota correta em vez de if ------
# a = int(input("primeiro bimestre: "))
# while a > 10:
#     a = int(input("Você digitou errado. Primeiro bimestre: "))
#
# b = int(input("segundo bimestre: "))
# while b > 10:
#     b = int(input("Você digitou errado.Segundo bimestre: "))
#
# c = int(input("terceiro bimestre: "))
# while c > 10:
#     c = int(input("Você digitou errado. Terceiro bimestre: "))
#
# d = int(input("quartoo bimestre: "))
# while d > 10:
#     d = int(input("Você digitou errado. Quarto bimestre: "))
#
# media = (a + b + c + d) / 4
# print("Media: {}".format(media))