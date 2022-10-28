x = 0
y = 0
sum = 0

def operator():
    z = input('input operation\n+, -, *, or /\n> ')
    if z == '+':
        print(str(x) + ' + ' + str(y) + ' = ' + str(x+y))
    elif z == '-':
        print(str(x) + ' - ' + str(y) + ' = ' + str(x-y))
    elif z == '*':
        print(str(x) + ' * ' + str(y) + ' = ' + str(x*y))
    elif z == '/':
        print(str(x) + ' / ' + str(y) + ' = ' + str(x/y))
    else:
        print('invalid input, please try again\n')
        operator()

#-------------------------------------------------------
        
x = float(input('input number 1\n> '))
y = float(input('input number 2\n> '))

operator()