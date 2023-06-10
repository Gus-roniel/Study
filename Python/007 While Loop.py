#WHILE LOOP
    # Usado para repeat a block code as long as the boolean expression for True
    # Syntax
# While boolean_expression:
    # statement
#Ex
n = 3
i = 1

while i <= n:
    print('Loop is easy')
    i = i+1 #mostra apenas 3 times because 4 is bigger

# Sum of Natural Numbers
n = 10
#Initialize sum and counter
sum = 0
i = 1
while i <=n:
    sum = sum+i
    i = i+1
print('A soma deu',sum)

# While loop com else
    # Quando the block code is False, irá para o else
    # Ex
counter = 0
while counter < 3:
    print('Inside Loop')
    counter = counter + 1
else:
    print('Inside else')

# Fazendo uma tabela matemática
n = 14
i = 1
while i <=10:
    print(n, 'x', i, '=', n*i)
    i = i+1