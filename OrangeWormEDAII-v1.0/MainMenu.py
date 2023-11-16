import StadisticsMenu
import cs
from datetime import datetime
import LoadingScreen
import time
import Sobreescribir
import checkRoute
import readUserRoutes
import showTraverseTime
import searchRoute
import writeUserRoutes

def menu(user, loginSys, subway, subwayDict, lineTimes):
    
    try:
        user.routeList = readUserRoutes.readUserRoutes(user)
    except:
        print("Aun no existe un archivo de rutas para el archivo")
        
    estado = True
    
    while(estado == True):
        
        hora = datetime.now().time()
        h = hora.hour
        m = hora.minute
        fecha = datetime.now().date()
        
        cs.clear()
        print(u"\u001b[38;5;202mMENU PRINCIPAL")
        print()
        
        print(u"\u001b[38;5;202m[1] MIS RUTAS")
        print(u"\u001b[38;5;202m[2] NUEVA RUTA")
        print(u"\u001b[38;5;202m[3] BUSCAR RUTA POR NOMBRE")
        print(u"\u001b[38;5;202m[4] ELIMINAR RUTA")
        print(u"\u001b[38;5;202m[5] CONSULTAR ESTADISTICAS")
        print(u"\u001b[38;5;202m[6] CAMBIAR CONTRASEÑA")
        print(u"\u001b[38;5;202m[7] CONSULTAR AVANCE DE TRENES")
        print(u"\u001b[38;5;202m[8] ELIMINAR CUENTA")
        print(u"\u001b[38;5;202m[9] CERRAR SESION")
        
        print()
        print(u"\u001b[38;5;46mBuen dia " + user.name) 
        print("HORA: ",f"{h:02d}:{m:02d}")
        print("FECHA: ",f"{fecha}")
        
        print(u"\u001b[0m")
        
        op = int(input("Ingresa la opcion a realizar: "))
        cs.clear()
        LoadingScreen.curiosidades()
        
        if (op == 1):
            user.printUserRoutes(subway, subwayDict)
            
        elif (op == 2):
            checkRoute.checkRoute(user, subway,subwayDict)
            
        elif (op == 3):
            if len(user.routeList) == 0:
                print(u"\u001b[38;5;196m¡Opcion invalida!")
                print(u"\u001b[0m")
                time.sleep(1.5)
            else:
                searchRoute.search(user.routeList, subway, subwayDict)
        
        elif(op == 4):
            cs.clear()
            toDel = input("Ingresa el nombre de la ruta a borrar: ")
            user.deleteRoute(toDel)
            writeUserRoutes.writeUserRoutes(user)

        elif (op == 5):
            StadisticsMenu.menuS()
            
        elif (op == 6):
            cs.clear()
            user.changePassword()
            Sobreescribir.sobreescribirUsuarios('accounts.txt',loginSys)

        elif (op == 7):
            print(u"\u001b[38;5;202mMENU PRINCIPAL")
            print(u"\u001b[0m")
            showTraverseTime.showTraverseTime(lineTimes)
         
        elif (op == 8):
            flag = user.deleteAccount() 
            if flag is True:
                loginSys.delete(user.name)
                Sobreescribir.sobreescribirUsuarios("accounts.txt", loginSys)
                estado = False
           
        elif (op == 9):
            estado = False
            
        else:
            print()
            print(u"\u001b[38;5;196m¡Opcion invalida!")
            print(u"\u001b[0m")
            time.sleep(0.7)
            
            
            