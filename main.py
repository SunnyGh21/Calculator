print('Calculator')

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

choice = input('Enter operation (+ or -): ')

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z


if choice == '+':
    result = add(x, y)
    z = result
    print(z)

elif choice == '-':
    result = subtract(x, y)
    z = result
    print(z)


