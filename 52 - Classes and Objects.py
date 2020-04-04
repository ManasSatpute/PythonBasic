class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


a = float(input('Enter any no. - '))
b = float(input('Enter any no. - '))
c=Calculator()
print('Sum is ',c.add(a,b))
print('Subtraction is ',c.sub(a,b))
print('Multiplication is ',c.mul(a,b))
print('Division is ',c.div(a,b))