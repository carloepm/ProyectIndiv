# se puede realizar la extracion de info de varias formas, uso Requests, que tiene dos metodos ( GET y POST)
# METODO GET

import requests
response = requests.get('https://diariochilecito.com')

contenido_html = response.text

print(contenido_html)




