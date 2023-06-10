# FOR LOOP
    # Usado para interações com outras sequências ou objetos interativos

# TIPOS DE SEQUÊNCIA
    # Strings: sequência de caracteres ('Hello World')
    # Lists: my_list = [2, "test", 5.6]
    # Range (): usado para criar uma sequência de números
        # Ex: numbers = range(1, 6) # cria uma seqência de 1 até 5

# FOR LOOP
    #Syntax:
        #FOR val IN sequence:
            #statement
# VAL é o nome qualquer dada para sequência
    #Ex:
languages = ['Java', 'Python', 'C++']
for item in languages:
    print(item)

# Ex: Sum 1 to 100
numbers = range(1,101)
sum = 0 # a valor da variável sum
for i in numbers:
    sum += i
print('Sum =', sum)

# Ex: Somar um número determinado número de vezes:
my_range = range(1,5)
a = 0
for val in my_range: 
    a = a + 1 # Será executado 4x o código, pois é a sequênia do range

# Ex: Multiplication Table
n = 14

for i in range(1,11):
    print(n, 'x', i, '=', n*i)

# FOR LOOP WHT ELSE
    # ELSE será usado quando o todos os itens do loop tiverem acabado
# Ex:
my_list = [5, 'Hello']

for item in my_list:
    print(item)
else:
    print('Inside else')

# BREAK STATEMENT
    # Usado para quebrar um loop
    # Um loop costuma continuar enquanto a expressão se mantiver verdadeira
    # o break é usado para interromper esse loop
# Ex
    # FOR LOOP
# for val in sequence:
#    ...
#    if test_expression:
#        break
#    ...

    # WHILE LOOP
# while text_expression1:
#    ...
#    if test_expression2:
#        break
#    ...

# BREAK 'is almost always' (é quase sempre) usado com IF

# Exemplo
numbers = [1, 5, 0, -4, 10, 9]

for val in numbers:

    if val < 0: #condicional para aplicar o break
        break
    print(val)

# Exemplo = Calculadora que soma números apenas positivos

sum = 0

while True:
    n = input ('Enter a number: ')
    n = float(n) #converter para float

    if n < 0:
        break
    sum += n

print('Sum =', sum)

# CONTINUE 
    # Serve para "pular" um remposável por interromper um loop
number = 0

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop') # mostrou todos os número de 1 a 10, pulando o número 5

# PASS
    # Usado para ignorar uma função que poderá ser usada no futuro
number = 0

for number in range(10):
    if number == 5:
        pass    # pass here

    print('Number is ' + str(number))

print('Out of loop') # ignorou a condicional, incluindo todos os número, inclusive o 5