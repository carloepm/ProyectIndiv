import random
import string

def generar_pass(longitud):
    caracteres =  string.digits + string.ascii_letters 
    # aqui puedo elegir si mi generador de pass incluira letras, numeros y/o simbolos 
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

long_deseada = int(input('Ingrese la longitud deseada para su contraseña:'))
contrasena_generada = generar_pass(long_deseada)

print('Contraseña generada: ', contrasena_generada)