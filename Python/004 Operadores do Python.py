# PYTHON OPERATORS

# ADIÇÃO (+)
    # Adição de números
a = 5
b = 3
sum = a + 10
print("O resultado é: ", sum)

a1 = 6
a2 = 4
a3 = 10
result = a1+a2+a3
print(result)
    # Concatenar objetos
        # Concatena two strings
first_name = "Jack"
last_name = "Low"
name = first_name + " " + last_name
print(name)

# SUBTRAÇÃO (-)
    # Subtração de números
a = 5
b = 3
sum = a - b
print("O resultado é: ", sum)

# MULTIPLICAÇÃO (*)
    # Multiplicação de números
a = 5
b = 3
sum = a * b
print("O resultado é: ", sum)
    # Multiplicação de string
a = 'foo'
b = a*3
#print(b) # sai foofoofoo

#a = 'foo'
#b = a*'3'
#print(b) # ERRO: não pode multiplicar sequencias do type "str"

# BARRA (/) E DUPLA BARRA (//)
    # Barra (/): usada para divisão
    # Barra dupla (//): encontrar o quociente instantaneamente
result1 = 14//3
print(result1) # resltado 4 (não mostra a sobra)

# PORCENTAGEM (%)
    # Resulta na sobra da divisão
result2 = 14%3
print(result2) # 14/3 = 12 (sobra 2)

# POTÊNCIA (**)
    # Resulta potenciação de determinada operação
a5 = 2
b5 = 5
result5 = a5**b5
print(result5) 

# IGUAL (=)
    # Usado para 'assign" (adicionar) valores as variáveis
    # Pode assign múltiplas variáveis 'at once' (de uma vez só)
    # a, b, c = 5, 3.2 , 'Hello'
    # a = b = c = "Hello

# x += 5 (equivale a x = x+5)
    # O mesmo vale para qualquer operação

# Os operadores seguem a precedência da Matemática

str = '4'
str2 = '3'
result = str2+str
print("o Sultado é: ", result)