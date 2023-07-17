# TUPLE
    # Similar a listas, com algumas diferenças:
        # Não pode mudar elementos
        # Entre (), separado por vírgulas (pode ser usado sem, mas é uma boa prática o seu uso)
# Similar a listas, podemos acessar itens dela com o uso de []
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[1]) # output 2
# também pode ser usado indexadores negativos para achar determinado item
# Uso de range para acessar lista de itens
print(my_tuple[1:3]) # (2, 3) mostrado entre parênteses

# Se dentro de uma tuple tiver uma lista, o item pode ser mudado
my_tuple = (1, 2, 3, ['a', 'b'], 4, 5, 6)
my_tuple[3][0] = 'x' # (1, 2, 3, ['x', 'b'], 4, 5, 6)
print(my_tuple)

# USING + AND *
odd = (1, 3, 5)
print(odd + (2,4)) # segue a ordem, pois é uma soma

letters = ('a', 'b')
print(letters*3)

# É possível porque não está mudando as tuples, mas criando tuples novas

# Não é possível deletar apenas um item de uma tuple (como em uma lista), apenas a tuple inteira

# COUNT (X)
    # Usado para contar quantas vezes aquele valor está na tuple
my_tuple = ('a', 'p', 'p', 'l', 'e')
result = my_tuple.count('p')
print(result) # string "p" aparece 2x na tuple

# INDEX(X)
    # Usado para saber onde está indexado o item (primeira vez)
result2 = my_tuple.index('l')
print(result2) # string "l" aparece na 3º posição da tuple

print('e' in my_tuple) # True - informe que string "e" está contida nessa tuple

for name in ('John', 'Kate'):
    print('Hello', name) # loop usado para cada item dentro da tuple