def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    if b==0:
        return'Cannot divide'
    else:
        return a/b 
a = int(input('Enter the first number\n'))
b = int(input('Enter the second number\n'))
print('Please select operation to perfom\n'
                '1: add\n'
                '2: subtract\n'
                '3: muiltiply\n'
                '4: division\n')

choose=int(input('Enter the operation which is to be selected:\n'))

if choose==1:
     print('The addition of',a,'and',b,'=',add(a,b))
elif choose==2:
    print('The subtraction of',a,'and',b,'=',subtract(a,b))
elif choose==3:
    print('The multiplication of',a,'and',b,'=',multiply(a,b))
elif choose==4:
    print('The division of',a,'and',b,'=',division(a,b))
else:
     print('Invalid operation')

