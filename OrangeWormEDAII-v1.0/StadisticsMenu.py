import LoadingScreen
import Graphs
import StatsTerminal
import cs
import time
from datetime import datetime

def menuS():
    
    estado = True
    erroneo = True
    
    while(estado == True):
        
        while(erroneo == True):
            
            hora = datetime.now().time()
            h = hora.hour
            m = hora.minute
            fecha = datetime.now().date()
            
            cs.clear()
            print(u"\u001b[38;5;208mMENU DE ESTADISTICAS DE FLUJO")
            print()
            print("HORA: ",f"{h:02d}:{m:02d}")
            print("FECHA: ",f"{fecha}")
            print()
            print(u"\u001b[38;5;163m[1] Flujo Linea 1")
            print(u"\u001b[38;5;20m[2] Flujo Linea 2")
            print(u"\u001b[38;5;94m[3] Flujo Linea 3")
            print(u"\u001b[38;5;115m[4] Flujo Linea 4")
            print(u"\u001b[38;5;214m[5] Flujo Linea 5")
            print(u"\u001b[38;5;196m[6] Flujo Linea 6")
            print(u"\u001b[38;5;166m[7] Flujo Linea 7")
            print(u"\u001b[38;5;35m[8] Flujo Linea 8")
            print(u"\u001b[38;5;94m[9] Flujo Linea 9")
            print(u"\u001b[38;5;126m[10] Flujo Linea A")
            print(u"\u001b[38;5;35m[11] Flujo L\u001b[38;5;102mi\u001b[38;5;35mn\u001b[38;5;102me\u001b[38;5;35ma \u001b[38;5;102mB")
            print(u"\u001b[38;5;136m[12] Flujo Linea 12")
            print(u"\u001b[38;5;208m[13] Flujo METRO")
            print(u"\u001b[0m[14] Regresar al menu principal")
            print()
            
            op = int(input("Ingresa la estadistica que desear ver: "))
            print()
            cs.clear()
            LoadingScreen.curiosidades()
            print()
            
            if(op > 0 and op < 15):
                erroneo = False
            else:
                print()
                print(u"\u001b[38;5;196m¡Opcion invalida!")
                print(u"\u001b[0m")
                time.sleep(0.7)
        
        if(op == 14):
            return
        
        erroneo = True
        
        while(erroneo == True): 
            print()
            cs.clear()
            print("[1] Ver las estadisticas como grafica de barras")
            print("[2] Ver las estadisticas en terminal")
            print()
            tipo = int(input("Ingresa el medio: "))
            print()
            cs.clear()
            LoadingScreen.curiosidades()
            print()
            
            if(tipo > 0 and tipo < 3):
                erroneo = False
            else:
                print()
                print(u"\u001b[38;5;196m¡Opcion invalida!")
                print(u"\u001b[0m")
                time.sleep(0.7)
        
        erroneo = True
        
        if(tipo == 1):
            if(op == 1):
                Graphs.linea1()
            elif(op == 2):
                Graphs.linea2()
            elif(op == 3):
                Graphs.linea3()
            elif(op == 4):
                Graphs.linea4()
            elif(op == 5):
                Graphs.linea5()
            elif(op == 6):
                Graphs.linea6()
            elif(op == 7):
                Graphs.linea7()
            elif(op == 8):
                Graphs.linea8()
            elif(op == 9):
                Graphs.linea9()
            elif(op == 10):
                Graphs.lineaA()
            elif(op == 11):
                Graphs.lineaB()
            elif(op == 12):
                Graphs.linea12()
            elif(op == 13):
                Graphs.flujoMetro()
        else:
            StatsTerminal.stats(op)
    
    
