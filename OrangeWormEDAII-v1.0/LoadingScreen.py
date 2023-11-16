import time
import random

def start():
    print(u"\u001b[38;5;202mEstacion Directa App [EDA METRO]")
    print(u"\u001b[38;5;202mBy Yordi Jimenez & Gustavo Valenzuela\u001b[0m")

    for i in range(1, 5):
        carga = "." * i
        print(f'\r\u001b[38;5;120mCargando recursos{carga}    ', end='', flush=True)
        time.sleep(0.5)
    
    
    for i in range(1, 5):
        carga = "." * i
        print(f'\r\u001b[38;5;120mIniciando aplicacion{carga}    ', end='', flush=True)
        time.sleep(0.5)

    for i in range(1, 5):
        carga = "." * i
        print(f'\r\u001b[38;5;120mTururu Proxima estacion, Login{carga}    ', end='', flush=True)
        time.sleep(0.5)
        
    print(u"\r\u001b[38;5;120mAplicacion lista, Bienvenidx :D\u001b[0m")
    print()

###############################################################################################
  
def login(state):
    carga = ["|", "/", "-", "\\"]
    print()
    for _ in range(10):
        for frame in carga:
            print(f"\rValidando credenciales {frame}", end="", flush=True)
            time.sleep(0.1)
    print()
    
    if(state == 0):
        print(u"\u001b[38;5;82m¡Sesion iniciada con exito!")
        
    elif(state == 1):
        print(u"\u001b[38;5;196m¡Contraseña incorrecta!")
    
    elif(state == 2):
        print(u"\u001b[38;5;196m¡ERROR!")
    
    elif(state == 3):
        print(u"\u001b[38;5;82m¡Se encontro el usuario en la BD!")
    
    elif(state == 4):
        print(u"\u001b[38;5;82m¡Usuario creado con exito!")
    
    elif(state == 5):
        print(u"\u001b[38;5;196m¡La contraseñas no coinciden!")
    
    elif(state == 6):
        print(u"\u001b[38;5;82m¡La contraseña se cambio con exito!")
        
    elif(state == 7):
        print()
                      
    
    print(u"\u001b[0m")

###############################################################################################

def curiosidades():
    
    curiosidades = [
        "Fue un 4 de septiembre de 1969 cuando comenzo a operar la Linea 1 del metro",
        "El STC Metro cuenta con una longitud de 226km",
        "En cada tren caben al rededor de 1020 personas",
        "El tren PMP68, fue el primer modelo en circular y fue disñado en Francia en 1968",
        "El desembarco de los primeros trenes tuvo lugar en el Puerto de Veracruz",
        "La linea mas profunda es la 7",
        "La linea 7 puede ser utilizada como bunker en caso de un ataque nuclear :0",
        "El hombre rata vive en la estacion 'La raza' de la linea 3 (NO INVESTIGUES MAS O TE VAN A DORMIR D:)",
        "Existen 195 estaciones en total, 115 son subterráneas, 54 de superficie y 26 elevadas",
        "El icono de la estacion pino suarez representa la piramide de Ehecatl (Se descrubrio en las escavaciones para la construccion de esta estacion)",
        "En 1990, la pelicula 'El vengador del futuro' utilizo la estacion chabacano para una escena de accion",
        "En 2018, el consumo total de energia del metro fue de 786,772,431 kW",
        "Los trenes son color naranja debido a que en ese entonces el color distintivo del Departamento del DF era naranja",
        "La iconografia del metro fue diseñada por Lance Wyman",
        "En 1978, mientras se construia la linea 4 se hallaron los restos de un mamut, estos estan exhibidos en la estacion Talisman de dicha linea",
        "Dentro de la estación La raza se encuentra el primer museo científico-cognoscitivo del mundo",
        "El 19 de junio de 1967 inició la construcción de la primera línea del metro",
        "El sistema de transporte colectivo cuenta con 383 trenes y 15 mil trabajadores",
        "Durante la construcción de la estación Balderas en 1968 se encontró el cráneo de un hombre cuya antigüedad data de hace 11 mil años",
        "En todas las líneas durante su construcción se encontraron al menos un objeto prehispánico",
        "El Ing. Bernardo Quintana fue quien presentó el proyecto del metro a las autoridades del Distrito Federal en 1958, fue rechazado por su elevado costo" 
    ]
    
    carga = ["|", "/", "-", "\\"]
    
    tmp = curiosidades[random.randint(0,len(curiosidades) - 1)]
    
    print("\u001b[38;5;51mSABIAS QUE...") 
    for _ in range(10):
        for frame in carga:
            print(f"\r{tmp} {frame}", end="", flush=True)
            time.sleep(0.1)
    
    print("\u001b[0m")
    
    
def search():
    carga = ["|", "/", "-", "\\"]
    print()
    for _ in range(10):
        for frame in carga:
            print(f"\rBuscando ruta {frame}", end="", flush=True)
            time.sleep(0.1)
    print()
    
def estacion():
    carga = ["|", "/", "-", "\\"]
    print()
    for _ in range(10):
        for frame in carga:
            print(f"\rBuscando estacion en el mapa del STC Metro {frame}", end="", flush=True)
            time.sleep(0.1)
    print()