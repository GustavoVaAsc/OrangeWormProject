import cs

def showTraverseTime(lineTimes):
    
    cs.clear()
    
    for i in range(0, len(lineTimes)):
        if (i == 0):
            color = '\u001b[38;5;163m'
        elif(i == 1):
            color = '\u001b[38;5;20m'
        elif (i == 2):
            color = '\u001b[38;5;94m'
        elif (i == 3):
            color = '\u001b[38;5;115m'
        elif (i == 4):
            color = '\u001b[38;5;214m'
        elif (i == 5):
            color = '\u001b[38;5;196m'
        elif (i == 6):
            color = '\u001b[38;5;166m'
        elif (i == 7):
            color = '\u001b[38;5;35m'
        elif (i == 8):
            color = '\u001b[38;5;94m'
        elif (i == 9):
            color = '\u001b[38;5;126m'
        elif (i == 10):
            color = '\u001b[38;5;102m'
        elif (i == 11):
            color = '\u001b[38;5;136m'

        print("{}Avance de trenes en la Linea {}: {} minutos".format(color,i+1,lineTimes[i]))
    
    print(u"\u001b[0m")
    
    state = 0
    
    while(state == 0):
        exit = int(input("Ingresa 1 para volver al menu principal: "))
        
        if(exit == 1):
            state = 1
        else:
            print(u"\u001b[38;5;196m¡Opcion invalida!\u001b[0m")