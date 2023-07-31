def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multi(a, b):
    return a * b

def divid(a, b):
    if b != 0:
        return a / b
    else:
        print('Error: no se puede dividir en 0')
        return None
    
def calcular():
    operacion = input('Que operacion deseas realizar? (+, -, *, /,): ')
    num1 = float(input('Ingresar el primero numero: '))
    num2= float(input('Ingresar el segundo numero: '))

    if operacion == '+':
        resultado = sumar(num1, num2)
    elif operacion == '-':
        resultado = restar(num1, num2)
    elif operacion == '*':
        resultado = multi(num1, num2)
    elif operacion == '/':
        resultado = divid(num1, num2)
    else:
        print('Operacion no valida')
        return
    
    print('El resultado es:', resultado)

calcular()
