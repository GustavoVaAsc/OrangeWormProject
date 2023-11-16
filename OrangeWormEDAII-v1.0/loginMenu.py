from readAccounts import readAccounts
from logUser import logUser
from register import register
import cs
from datetime import datetime
import LoadingScreen
import time

def loginMenu(loginSys):
    readAccounts(loginSys)
    flag = False
    
    while flag == False:
        
        hora = datetime.now().time()
        h = hora.hour
        m = hora.minute
        fecha = datetime.now().date()
        
        cs.clear()
        
        ch = 0
        
        print(u"\u001b[38;5;202mTururu, Proxima estacion: Facultad de Ingenieria ;)")
        print()
        print("HORA: ",f"{h:02d}:{m:02d}")
        print("FECHA: ",f"{fecha}")
        print()

        print(u'\u001b[38;5;120m[1] INICIAR SESION')
        print(u'\u001b[38;5;120m[2] REGISTRARSE')
        print(u'\u001b[38;5;120m[3] SALIR\u001b[0m')
        print()
        
        
        ch = int(input("Ingresa la opcion que deseas realizar: "))
        
        cs.clear()
        
        if ch == 1:
            LoadingScreen.curiosidades()
            cs.clear()
            acc = logUser(loginSys)
            if acc is not None:
                return acc
        elif ch == 2:
            LoadingScreen.curiosidades()
            cs.clear()
            register(loginSys)
            flag = False
        elif ch == 3:
            print(u"\u001b[38;5;196mTururu, se te fue el metro, adios D:")
            print(u"\u001b[0m")
            return None
        else:
            print(u"\u001b[38;5;196mEntiendo que estes transbordando y por ello ingresaste una opcion invalida, no te proecupes :D")
            print(u"\u001b[0m")
            time.sleep(3.0)
        