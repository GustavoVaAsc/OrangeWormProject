import time
import cs
import LoadingScreen

def search(l,subway,subwayDict):
    cs.clear()
    print(u"\u001b[38;5;202mBUSCAR RUTA POR NOMBRE")
    print(u"\u001b[0m")
    route_name = input("Ingresa el nombre de la ruta: ")
    
    LoadingScreen.search()
    print()
    
    for node in l:
        if node.name == route_name:
            print(u"\u001b[38;5;3mNombre de la ruta: " + node.name + "\u001b[0m")
            node.firstStation,node.lastStation = subway.printRoute(subwayDict[node.firstStation],subwayDict[node.lastStation])
            print()
            print("Numero de estaciones de la ruta: "+ str(node.stationNum))
            print()
            state = 0
            
            while(state == 0):
                exit = int(input("Ingresa 1 para volver al menu principal: "))
                
                if(exit == 1):
                    state = 1
                else:
                    print(u"\u001b[38;5;196m¡Opcion invalida!\u001b[0m") 
            
        else:
            print(u"\u001b[38;5;196mNo se encontro la ruta " + route_name + "\u001b[0m")
            time.sleep(1.5)
            return