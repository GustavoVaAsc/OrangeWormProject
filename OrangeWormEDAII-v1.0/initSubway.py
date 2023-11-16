# -*- coding: utf-8 -*-

from StationInfo import StationInfo
from Graph import Graph
import random
import cs

def readStationInfo(file_path,i):
    station_list = []
    
    with open(file_path, 'r', encoding = 'utf-8') as file:
        # Skip the header line
        next(file)
        
        for line in file:
            data = line.strip().split(',')
            station_name, transfer, station_id,cost, flu = map(str.strip, data)
            
            # Convert strings to appropriate types
            station_id = int(station_id)
            cost = int(cost)
            line = i
            
            # Create a StationInfo object and append it to the list
            station = StationInfo(station_id, station_name, line, transfer, cost)
            station_list.append(station)
    
    return station_list



def insertInGraph(graph,line,route,subwayDict):
    
    
    graph.addEdge(line[0].id,line[0].id,line[0].cost,False,line[0].stationName,line[0].stationName,route,route,line[0].transfer)
    for i in range(len(line)):
        if i == len(line) - 1:
            subwayDict[line[i].stationName] = line[i].id
            break
        if subwayDict.get(line[i].stationName) is None:
            subwayDict[line[i].stationName] = line[i].id
            graph.addEdge(line[i].id,line[i+1].id,line[i+1].cost,False,line[i].stationName,line[i+1].stationName,route,route,line[i+1].transfer)
        else:
            graph.addEdge(line[i].id,line[i+1].id,line[i+1].cost,False,line[i].stationName,line[i+1].stationName,route,route,line[i+1].transfer)
    graph.addEdge(line[len(line)-1].id,line[len(line)-1].id,line[len(line)-1].cost,False,line[len(line)-1].stationName,line[len(line)-1].stationName,route,route,line[len(line)-1].transfer)



def initSubway():
    cs.clear()
    subway = Graph(163,151,False,True)
    subwayDict = {}
    for i in range (1,13):
        l = 'Linea'
        if i == 10:
            aux = "A"
            path = l + ""+aux+".csv"
        elif i == 11:
            aux = "B"
            path = l + ""+aux+".csv"
        else:
            path = l + ""+str(i)+".csv"
        #print(path)
        toInsert = readStationInfo(path,i)
        insertInGraph(subway,toInsert,i,subwayDict)
    
    
    choice = 0
    print("[1] Ingresar tiempo de traslado manualmente")
    print("[2] Ingresar el tiempo de traslado aleatoriamente")
    print()
    print(u"\u001b[38;5;3mNota, al seleccionar la opcion 2 estas consciente que se tomaran tiempos promedios aproximados")
    print("Estos promedios van de 4 a 7 minutos")
    print(u"\u001b[0m")
    
    choice = int(input("Ingresa el metodo de entrada: "))
    
    lineTimes = []
    
    if choice == 1:
        for i in range(1,13):
            if i == 10:
                tmp = int(input('Ingresa el tiempo de la linea '+"A"+": "))
            elif i == 11:
                tmp = int(input('Ingresa el tiempo de la linea '+"B"+": "))
            else:
                tmp = int(input('Ingresa el tiempo de la linea '+str(i)+": "))
            lineTimes.append(tmp)
    else:
        for i in range(1,13):
            tmp = random.randint(4,7)
            lineTimes.append(tmp)
            
    subway.updateAllEdgesCosts(lineTimes)
    #subway.printRoute(1,21)
    cs.clear()
    return subway,subwayDict,lineTimes