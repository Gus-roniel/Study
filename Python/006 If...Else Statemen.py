# IF STATEMENT
    # Syntax

#if boolean_expression
#    statement(s) 
# Usar indentação para definir o block code 
number = 5 #exemplo
if number > 0:
    print('Number is positive') # apenas aparecerá se cumprir o requisito (fosse menor que zero, nao aparecia)
print("Aqui sempre será executado") # Está fora da indentação, 'hence' (por isso) sempre aparece

# IF...ELSE
# Syntax:
    # if boolean_expression:
    #   statement
    # else:
    #   statement
number = -5 #exemplo
if number > 0:
    print('Number is positive')
else:
    print('Number is negative')

# IF...ELIF...ELSE
    # Syntax:
    # if boolean_expressiona1:
    #   statement (s)
    # elif boolean_expressiona1:
    #   statement (s)
    # else:
    #   statement (s)
number = 0 #exemplo
if number > 0:
    print('Number is positive')
elif number == 0:
    print ('Equal zero')
else:
    print('Number is negative')

# NESTE IF...ELSE
# Criar um if...else dentro de um if...else (chamado de nidificação = nesting)
num = float(input('Enter the number: '))
if num >= 0:
    if num == 0:
        print ('Equal zero')
    else:
        print('Positive number')
else:
    print('Number is negative')