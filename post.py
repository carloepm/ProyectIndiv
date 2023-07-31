#METODO POST

import requests

datos = {"nombre": "carlos", "correo": "carlos@ejemplo.com"}


response = requests.post('https://diariochilecito.com', data=datos)

contenido_resp = response.text

print(contenido_resp)