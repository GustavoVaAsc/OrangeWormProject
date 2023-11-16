import LoadingScreen
import time
import cs
import os


class User:
    name = ""
    password = ""
    isAdmin = False
    routeList = []
    
    def __init__(self,name,password,isAdmin,routeList=[]):
        self.name = name
        self.password = password
        self.isAdmin = isAdmin
        self.routeList = []
        
    def login(self):
        logpassword = input('\u001b[38;5;120mContraseña:\u001b[0m ')

        if logpassword != self.password:
            LoadingScreen.login(1)
            time.sleep(1.5)
            print()
            return False
        else:
            LoadingScreen.login(0)
            print("Bienvenido! " + self.name)
            time.sleep(1.5)
            print()
            return True
        
    def changePassword(self):
        print(u"\u001b[38;5;202mCAMBIO DE CONTRASEÑA")
        print(u"\u001b[0m")
        logpassword = input('Insrese su contraseña actual: ')
        if logpassword != self.password:
            LoadingScreen.login(1)
            time.sleep(1.5)
            return False
        else:
            LoadingScreen.login(7)
            confirm = ""
            logpassword = input("Ingrese la nueva contraseña: ")
            confirm = input("Confirme la nueva contraseña: ")
            if logpassword == confirm:
                self.password = confirm
                
                LoadingScreen.login(6)
                time.sleep(1.5)
                return True
            else:
                LoadingScreen.login(5)
                time.sleep(1.5)
                return False
            
    def addRoute(self,route):
        self.routeList.append(route)
    
    
    def printUserRoutes(self,subway,subwayDict):
        
        cs.clear()
        
        if len(self.routeList) == 0:
            print(u"\u001b[38;5;3m¡Aun no tienes rutas guardadas!\u001b[0m")
            time.sleep(1.5)
            return
        else:
            for route in self.routeList:
                print(u"\u001b[38;5;3mNombre de la ruta: " + route.name + "\u001b[0m")
                t,st = subway.printRoute(subwayDict[route.firstStation],subwayDict[route.lastStation])
                route.transferTime = t
                print("Numero de estaciones de la ruta: "+ str(route.stationNum))
                print()
            
            print()
            print("[1] Ordenar por nombre")
            print("[2] Ordenar por tiempo de traslado")
            print("[3] Ordenar por numero de estaciones")
            print("[4] Ninguno")
            
            op = int(input("Ingresa la opcion a realizar: "))
            
            cs.clear()
            LoadingScreen.curiosidades()
            cs.clear(
                
            )
            if op == 1:
                self.sortAlphabetical()
                for route in self.routeList:
                    print(u"\u001b[38;5;3mNombre de la ruta: " + route.name + "\u001b[0m")
                    t,st = subway.printRoute(subwayDict[route.firstStation],subwayDict[route.lastStation])
                    route.transferTime = t
                    print("Numero de estaciones de la ruta: "+ str(route.stationNum))
                    print()
                
                tmp = False
                
                while tmp == False:
                    op = int(input("Ingresa 1 para regresar al menu principal: "))
                    if op == 1:
                        tmp = True
                    else:
                         print(u"\u001b[38;5;196mOpcion no valida\u001b[0m")
                         print()
                    
            elif op == 2:
                self.sortByTime()
                for route in self.routeList:
                    print(u"\u001b[38;5;3mNombre de la ruta: " + route.name + "\u001b[0m")
                    t,st = subway.printRoute(subwayDict[route.firstStation],subwayDict[route.lastStation])
                    route.transferTime = t
                    print("Numero de estaciones de la ruta: "+ str(route.stationNum))
                    print()
                    
                tmp = False
                
                while tmp == False:
                    op = int(input("Ingresa 1 para regresar al menu principal: "))
                    if op == 1:
                        tmp = True
                    else:
                         print(u"\u001b[38;5;196mOpcion no valida\u001b[0m")
                         print()
                         
            elif op == 3:
                self.sortByStationNum()

                for route in self.routeList:
                    print(u"\u001b[38;5;3mNombre de la ruta: " + route.name + "\u001b[0m")
                    t,st = subway.printRoute(subwayDict[route.firstStation],subwayDict[route.lastStation])
                    route.transferTime = t
                    print("Numero de estaciones de la ruta: "+str(route.stationNum))
                    print()
                
                tmp = False
                
                while tmp == False:
                    op = int(input("Ingresa 1 para regresar al menu principal: "))
                    if op == 1:
                        tmp = True
                    else:
                         print(u"\u001b[38;5;196mOpcion no valida\u001b[0m")
                         print()
                         
            else:
                return
                


    def sortAlphabetical(self):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i].name < arr[l].name:
                largest = l

            if r < n and arr[largest].name < arr[r].name:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)

        heapSort(self.routeList)


    def sortByStationNum(self):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i].stationNum < arr[l].stationNum:
                largest = l

            if r < n and arr[largest].stationNum < arr[r].stationNum:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
        
        heapSort(self.routeList)
                
    def sortByTime(self):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i].transferTime < arr[l].transferTime:
                largest = l

            if r < n and arr[largest].transferTime < arr[r].transferTime:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
        
        heapSort(self.routeList)
    
    
    def deleteRoute(self, route_name):
        route_to_delete = None

        for route in self.routeList:
            if route.name == route_name:
                route_to_delete = route
                break

        if route_to_delete is not None:
            print()
            confirm = int(input(f"Segurx que quieres borrar la ruta: '{route_name}'? (1- Si / 2- No): "))
            if confirm == 1:
                self.routeList.remove(route_to_delete)
                print()
                print(f"\u001b[38;5;82mRuta '{route_name}' borrada con éxito.\u001b[0m")
                time.sleep(1.5)
                return True
            else:
                print()
                print(u"\u001b[38;5;3mBorrado cancelado.\u001b[0m")
                time.sleep(1.5)
                return False
        else:
            print()
            print(f"\u001b[38;5;196mRuta '{route_name}' no encontrada.\u001b[0m")
            time.sleep(1.5)
            return False
    
    def deleteAccount(self):
        cs.clear()
        confirm_password = input("Ingresa tu contraseña: ")

        if confirm_password == self.password:
            print()
            confirm = int(input("Estás seguro de querer borrar tu cuenta? (1-Si/ 2-No): "))
            if confirm == 1:
                print(u"\u001b[38;5;82mCuenta borrada con éxito.\u001b[0m")
                print()
                file_name = self.name +"Routes.txt"

                file_path = os.path.join(os.getcwd(), file_name)

                try:
                    os.remove(file_path)
                    print(f"\u001b[38;5;82mFile '{file_path}' deleted successfully.\u001b[0m")
                except OSError as e:
                    print(f"\u001b[38;5;196mError deleting file:\u001b[0m {e}")
                
                time.sleep(3)      
                return True
            else:
                print()
                print(u"\u001b[38;5;3mCancelado el borrado de la cuenta\u001b[0m")
                time.sleep(1.5)
                return False
        else:
            print()
            print(u"\u001b[38;5;196mContraseña incorrecta.\u001b[0m")
            time.sleep(1.5)
            return False
        