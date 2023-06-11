# FUNCTIONS
    # Ajudam a quebrar nosso programa em pedaços menores e modulares
    # Fazem ele mais organizado e gerenciável
    # Usado para padronizar funções que se repetem dentro do código

# COMO CRIAMOS UMA FUNÇÃO (Syntax)
# def function_name(parameters):
#    statement(s)

# DEF = marca o início do cabeçalho da função
# function_name = nome usado para identificar a função
# parameters = usado para passar os valores da função (são opcionais)
# dois pontos = marca o término da função header
# o corpo da função é feito de um ou mais declarações
# a função pode ter um "return" statement (também opcional) - usado para mandar para fora o valor

"""# Ex:
def saudacao(name, last_name): # itens dentro do parênteses são as variáveis que devem ser inclusas
    print(f"Hello {name} {last_name}") # f fora das aspas para indicar que será usado uma função
    # usar {} no meio de strings para colocar as variáveis


name = input('Qual é seu nome? ')
last_name = input('Qual seu sobrenome? ')
print(saudacao(name, last_name)) # não precisa return, pois não manda pra fora nenhum dado"""

def soma(num1,num2,num3): # se valor não for definido dentro da função, será usado o valor definido depois
    soma1 = num1+num2+num3
    return soma1

print('O campeão fez ', soma(5,8,9) ) # usado return para puxar valo para função # valor definido no parenteses
# não colocando o return, ele mostraria NONE

def soma(num1,num2,num3): # se valor for definido dentro da função, será usado o valor dentro da função
    num1 = 2
    num2 = 2
    num3 = 2
    soma1 = num1+num2+num3
    return soma1

print('O campeão fez ', soma(5,8,9) ) # usado return para puxar valo para função
# não colocando o return, ele mostraria NONE

def numero_absoluto (numero):
    if numero >= 0:
        return numero
    else:
        return -numero
    
print(numero_absoluto(2))
print(numero_absoluto(-2))
print(numero_absoluto(-5.2))

# VARIÁVEL GLOBAL = fora da função
# VARIÁVEL LOCAL = dentro da função

# ADD ARGUMENTO PADRÃO PARA FUNÇÕES
def saudacao(name, msg = "Good morning"):
    print("Olá", name + ", " + msg)

saudacao("Kate") # manterá a mensagem padrão da função
saudacao("Bruce", "tudo certo?") # trocará a mensagem padrão pela escrita

# argumentos devem seguir a ordem correta, não podendo ser trocados
"""def saudacao(msg = "Good morning", name):
    print("Olá", name + ", " + msg)
saudacao("Kate") # não dará certo pois não está na ordem"""

saudacao(msg = "tudo certo?",name ="Bruce",  ) # dando o nome certo, a ordem não interfere
# podemos nomear também apenas um argumento

# Quando não sabemos a quantidade de argumentos que será usado na função, usamos *
def greet(*names):
    print(names)

greet("joão", "cecilia", "leandro")
# estão dentro de uma sequência antes de ser passado para função

# FUNÇÃO LAMBDA (OU ANÔNIMA)
    # Usada para realizar uma função sem nome
    # Syntax:
    # quando precisamos de uma função sem nome por um curto espaço de tempo
# lambda arguments: expression
quadrado = lambda x: x * x
result = quadrado(5)
print(result) # passa resultado mais direto, sem precisar fazer DEF
# normalmente usada junto com funções como FILTER(), MAP()

# RECURSION
    # Usado quando uma expressão chama ela mesma
    # para impedir um loop infinito, usamos IF...ELSE
def calc_sum(n):
    if n==1:
        return 1
    else:
        return n + calc_sum(n-1)
    
sum = calc_sum(3)
print(sum)