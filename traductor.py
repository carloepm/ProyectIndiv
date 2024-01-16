from googletrans import Translator

traductor = Translator()

languague = {"bn": "Bangladesh",
             "en": "Ingles",
             "ko": "Coreano",
             "fr": "Frances",
             "de": "Aleman",
             "he": "Hebreo",
             "hi": "Hindue",
             "it": "Italiano",
             "ja": "Japones",
             "la": "Latin",
             "ms": "Malasia",
             "ne": "Nepal",
             "ru": "Ruso",
             "ar": "Arabico",
             "zh": "Chino",
             "es": "Español"}
             
allow = True #variable para controlar el lenguaje correcto en el input

while allow:
    
    user_code = input(f"Ingrese el idioma que desea traducir, para ver el listado de idiomas ingrese 'opciones'\n")

    if user_code == "opciones": #esto muestra las opciones de idiomas
        print("code: lenguaje")
        for i in languague.items():
            print(f"{i[0]} => {i[1]}")
        print()
    
    else: #validar input del usuario
        for lan_code in languague.keys():
            if lan_code == user_code:
                print(f"Has seleccionado un idioma {languague[lan_code]}")
                allow = False
        if allow:
            print("No es un codigo de idioma valido!")

while True: #iniciado loop de traductor
    string = input("\n Escribe el texto que quieres traducir: \nPara salir del programa, escribe 'close'\n")
     
    if string == "close": #salir del programa
        print(f"\nNos vemos pronto!")
        break
    
    #metodo traductor de googletrans
    translated = traductor.translate(string, dest=user_code)
    #print traduccion
    print(f"\n{languague[user_code]} traduccion: {translated.text}")
    #print pronunciacion
    print(f"Pronunciacion: {translated.pronunciation}")
    
    for i in languague.items():
        if translated.src == i[0]:
            print(f"Traducido desde: {i[1]}") 
   
    
    













