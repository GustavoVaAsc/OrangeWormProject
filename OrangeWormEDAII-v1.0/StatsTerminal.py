import csv
import cs

def stats(linea):
    cs.clear()
    
    if (linea == 1):
        archivo = 'Linea1.csv'
        color = '\u001b[38;5;163m'
        num = 'Linea 1'
    elif (linea == 2):
        archivo = 'Linea2.csv'
        color = '\u001b[38;5;20m'
        num = 'Linea 2'
    elif (linea == 3):
        archivo = 'Linea3.csv'
        color = '\u001b[38;5;94m'
        num = 'Linea 3'
    elif (linea == 4):
        archivo = 'Linea4.csv'
        color = '\u001b[38;5;115m'
        num = 'Linea 4'
    elif (linea == 5):
        archivo = 'Linea5.csv'
        color = '\u001b[38;5;214m'
        num = 'Linea 5'
    elif (linea == 6):
        archivo = 'Linea6.csv'
        color = '\u001b[38;5;196m'
        num = 'Linea 6'
    elif (linea == 7):
        archivo = 'Linea7.csv'
        color = '\u001b[38;5;166m'
        num = 'Linea 7'
    elif (linea == 8):
        archivo = 'Linea8.csv'
        color = '\u001b[38;5;35m'
        num = 'Linea 8'
    elif (linea == 9):
        archivo = 'Linea9.csv'
        color = '\u001b[38;5;94m'
        num = 'Linea 9'
    elif (linea == 10):
        archivo = 'LineaA.csv'
        color = '\u001b[38;5;126m'
        num = 'Linea A'
    elif (linea == 11):
        archivo = 'LineaB.csv'
        color = '\u001b[38;5;102m'
        num = 'Linea B'
    elif (linea == 12):
        archivo = 'Linea12.csv'
        color = '\u001b[38;5;136m'
        num = 'Linea 12'
    elif (linea == 13):
        archivo = 'METRO.csv'
        color = '\u001b[38;5;208m'
        num = 'METRO'
    else:
        return
    
    flujo = []
    nombres = []
    
    with open(archivo, 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    state = 0
    
    print(F'{color}{num}')
    print()
    
    if(linea != 13):
        print("\u001b[0mESTACION - FLUJO TOTAL (MILLONES)")
    else:
        print("\u001b[0mLINEA - FLUJO TOTAL (MILLONES)")
    print()
    
    for nombre, f in zip(nombres, flujo):
        ent = int(f)
        print(f'{color}{nombre} \u001b[0m- {color}{f} {"*" * ent}')
        
    print(u"\u001b[0m")    
    while(state == 0):
        exit = int(input("Ingresa 1 para volver al menu de estadisticas: "))
        
        if(exit == 1):
            state = 1
        else:
            print(u"\u001b[38;5;196m¡Opcion invalida!\u001b[0m")
    