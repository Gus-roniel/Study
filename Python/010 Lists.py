#LISTS
    #Criada no lugar de itens dentro de colchetes [square brackets], separeted by commas (vírgulas)
# numbers [2, 5, 10]
# pode contem qualquer item, inclusive outras listas
# numbers [2, 5, 10, [names]]

# podemos acessar elementos da lista using []
    # ordem dos caracteres começa no [0], não no [1]
    # pode-se usar indexadores negativos para buscar item da lista de trás para frente, começando pelo [-1]
    # podemos pegar uma parte da lista usando colchetes e dois pontos
my_list = ["p", "y", "t", "h", "o", "n"]
print(my_list[0:2]) # pega o primeiro e não pega o último item
print(my_list[3:]) # começando do quarto item até o fim
print(my_list[:-3]) # pega do primeiro normal até o item -3
print(my_list[:]) # todos os itens da lista

# mudar itens da lista
    # we can change numbers a list
odd = [2, 4, 6, 8]
odd[0] = 12
print(odd) # [12, 4, 6, 8]

odd[1:4] = [3, 5, 7]
print(odd) # [12, 3, 5, 7]

# add elements to a list
odd.append(7)
print(odd) #[12, 3, 5, 7, 7]
odd.extend([11, 15, 17]) # add a list inside other list
print(odd) #[12, 3, 5, 7, 7, 11, 15, 17]

# using + and * operators
odd = [1,3,5]
print(odd+[7, 9, 11]) # combina as duas listas
print(['a', 'b']*3) # repeat itens of a list

odd = [1, 9]
odd.insert(0, 5)
print(odd) # [5, 1, 9] - insere o segundo número no lugar referente ao primeiro
odd[2:2] = [5, 7] # inserindo a lista a partir do 3º item da lista
print(odd)

# deletando itens da lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del my_list[2] # exclui o 3º item da lista
del my_list[1:5] # deleta o intervalo entre segundo item até o quarto 
del my_list # deleta lista inteira

# podemos usar REMOVE() and POP()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.remove(3) # remove especificamente o número 3 da lista (não o 4º item)
print(my_list)

print(my_list.pop(1)) # retira e exibe o item que foi retirado na 2º colocação
print (my_list) # exibindo lista depois do item popped
print(my_list.pop()) # retira e exibe o item que foi retirado na última colocação
my_list.clear() # limpa a lista

#MÉTODOS DE CÓPIA DE LISTAS
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = my_list # o que for mudado em uma lista, mudará automaticamente na outra

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = my_list.copy() # o que for mudado na primeira lista, não altera na segunda

# INSERIR LOOPS NA LISTA
for fruit in ['apple', 'banana', 'mango']:
    print(" I like", fruit) # usanos o nome dado para cada item da lista

# CHECAR SE DETERMINADO ITEM ESTÁ NA LISTA
my_list = ["p", "y", "t", "h", "o", "n"]
print('p' in my_list) # True
print('o' in my_list) # True
print('P' in my_list) # False (case sensitive)

# PEGAR ITEM DE UMA LISTA-ITEM DENTRO DE OUTRA LISTA
my_list = [1, 2, 3, [1, 2, 3, 4]]
result = my_list[3][1] # pegou o 4º item da lista (uma lista) e depois pegou o 2º item
print(result) 

result = my_list[3] # pegou a lista inteira
print(result)