a = 10
b = 6

soma = a+b
print('soma =', soma)

sub = a - b
print('subtracao:', sub)

mult = a*b
print('multiplicacao', mult)

div = a/b
print('divisao', div)

resto = a % b
print('resto:', resto)

print(type(soma)) #informa o tipo da variavel <int>

soma = str(soma)
print(type(soma)) #aqui já está como <string>

print('soma: ' + str(soma)) #concatenou a palavra 'soma' com o valor

print(type(div)) #informa o tipo da variavel <float>

# ------- conversão de número
x = '1'
soma2 = int(x) + 1 #converteu de string para inteiro
print(soma2)


print('soma: {}'.format(soma)) #concatena dentro da string


print('soma: {}. \nsubtração: {}. \nmultiplicacao:{}. '
      '\ndivisao: {}. \nresto: {} '.format(
    soma,sub,mult,div,resto)) #respeitar a ordem

# ----- entrada de dados ------

c = int(input('Entre com um valor:')) #necessário determinar antes <int> porque
# se não fica como string
d = int(input('Entre com outro valor:'))



resultado = c+d

print('O total dos valores é igual a:', resultado )