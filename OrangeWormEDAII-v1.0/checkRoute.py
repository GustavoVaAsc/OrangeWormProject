from Route import Route
import cs
import LoadingScreen
import time
import writeUserRoutes

def checkRoute(user, subway,subwayDict):
    cs.clear()
    
    startP = input(u"\u001b[38;5;3mIngresa la estacion de origen:\u001b[0m ")
    startP = startP.upper()
    
    LoadingScreen.estacion()
    print()
    
    if subwayDict.get(startP) is None:
        print(u"\u001b[38;5;1mIngresaste un nombre de estación inválido!\u001b[0m")
        time.sleep(1.5)
        return
    endP = input(u"\u001b[38;5;3mIngresa la Estacion de destino:\u001b[0m ")
    endP = endP.upper()
    
    LoadingScreen.estacion()
    
    if subwayDict.get(endP) is None:
        print(u"\u001b[38;5;1mIngresaste un nombre de estación inválido!\u001b[0m")
        time.sleep(1.5)
        return
    elif endP == startP:
        print(u"\u001b[38;5;1mLas estaciones son las mismas D:!\u001b[0m")
        time.sleep(1.5)
        return 
    
    cs.clear()
    LoadingScreen.curiosidades()
    cs.clear()
    
    trTime, stNum = subway.printRoute(subwayDict[startP], subwayDict[endP])
    
    print("[1] Si")
    print("[2] No")
    op = int(input("Deseas guardar la ruta en tus favoritas?: "))
    if op == 1:
        nm = input("Ingresa el nombre de la ruta (Casa, Trabajo, Escuela, etc): ")
        newRoute = Route(nm,startP,endP,trTime,stNum)
        user.routeList.append(newRoute)
        writeUserRoutes.writeUserRoutes(user)
        
    else:
        return  