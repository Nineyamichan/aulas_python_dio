
# ----------- Teste de impar/par --------

#a = int(input("Informe um valor: "))

#resto = a % 2

#if resto == 0:
#    print("O número é par: {}".format(resto))
#else:
#    print("O número é ímpar: {}".format(resto))

# ------------- comparativo ------------

#a = int(input("Informe o valor 1: "))
#b= int(input("Informe o valor 2: "))

#resto_a = a % 2
#resto_b = b % 2

#if resto_a == 0  or resto_b == 0: #operador "not" inverte a logica!
#    print("Foi digitado um número par de valor: {}".format(a,b))

#else:
#    print("Nenhum número par")


#----------- validação de nota ---------

a = int(input("primeiro bimestre: "))
if a > 10:
    a = int(input("Você digitou errado. Primeiro bimestre: "))

b = int(input("segundo bimestre: "))
if b > 10:
    b = int(input("Você digitou errado.Segundo bimestre: "))

c = int(input("terceiro bimestre: "))
if c > 10:
    c = int(input("Você digitou errado. Terceiro bimestre: "))

d = int(input("quartoo bimestre: "))
if d > 10:
    d = int(input("Você digitou errado. Quarto bimestre: "))

media = (a + b + c + d) / 4
print("Media: {}".format(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print("Media: {}".format(media))
#
# else:
#     print("Foi informado alguma nota com erro")
#


