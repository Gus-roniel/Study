# TIPOS DE CONVERSÃO
    #Conversão implícita    
        #Python converte automaticamente 
a = 2 #integer
b = 2.5 #float
sum = a+b # Função SUM = usado para somar um conjunto dentro de um determinado conjunto
print(sum) # Converteu e somou sozinho um número integer com um float

# Função type()
    # Usado para saber o tipo de variável
a = 2 #integer
b = 2.5 #float
sum = a+b 
print("O tipo da variável é: ", type(sum)) # output: O tipo da variável é:  <class 'float'>
        #Cuidar a vírgula no print, com variáveis diferentes

# FUNÇÕES PARA CONVERTER:
    # int () = converter para integer (remove a parte decimal - arredonda sempre para baixo)
    # float () = converter para float
    # str() = converter para string
f = 1.23
print(int(f)) 

# ERROS DE CONVERSÃO
    # Não é possível converter palavras em caracteres numéricos
# Ex1: 
a1 = 'Hello World'
print(int(a1)) # output: invalid literal for int()
    # Converter string numérico para type que não faz parte
# Ex2:
a2 = "55.5"
print(int(a2)) # output: invalid literal for int()
# Para float poderia ser convertido, por ser do mesmo type