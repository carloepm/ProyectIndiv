import datetime
import time


def config_alarm():
    hora_alarma = input('Ingresa la hora de la alarma (formato HH:MM):')
    hora_alarma = datetime.datetime.strptime(hora_alarma, '%H:%M').time()
    
    return hora_alarma

def act_alarm(hora_alarma):
    

    while True:
        hora_actual = datetime.datetime.now().time()
        if hora_actual >= hora_alarma:
            print('!Alarma Activada!')
            # aca puedo agregar codigo para reproducir algun sonido o ejecutar alguna accion
          
            break
        time.sleep(1) 

hora_alarma = config_alarm()
act_alarm(hora_alarma)

