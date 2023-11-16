import matplotlib.pyplot as plt
import csv

def flujoMetro():
    
    flujo = []
    
    with open('METRO.CSV', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo']) 
            flujo.append(f)
    

    colores = ['#E4007C','#0000FF','#556B2F','#00FFFF','#FFFF00','#FF0000','#FFA500','#008000','#A52A2A','#800080','#808080','#FFD700']
    nombres = ['L1','L2','L3','L4','L5','L6','L7','L8','L9','LA','LB','L12',]

    plt.bar(nombres, flujo, color = colores)
    
    plt.xlabel('Linea')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas en el STC Metro (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
    
    plt.show()

#############################################################################################################
   
def linea1():
    
    flujo = []
    nombres = []
    
    with open('Linea1.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#E4007C'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 1')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 1 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################

def linea2():
    
    flujo = []
    nombres = []
    
    with open('Linea2.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#0000FF'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 2')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 2 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()
 
############################################################################################################# 
   
def linea3():
    
    flujo = []
    nombres = []
    
    with open('Linea3.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#556B2F'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 3')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 3 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################
    
def linea4():
    
    flujo = []
    nombres = []
    
    with open('Linea4.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#00FFFF'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 4')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 4 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################
    
def linea5():
    
    flujo = []
    nombres = []
    
    with open('Linea5.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#FFFF00'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 5')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 5 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################
    
def linea6():
    
    flujo = []
    nombres = []
    
    with open('Linea6.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#FF0000'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 6')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 6 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################

def linea7():
    
    flujo = []
    nombres = []
    
    with open('Linea7.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#FFA500'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 7')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 7 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################

def linea8():
    
    flujo = []
    nombres = []
    
    with open('Linea8.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#008000'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 8')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 8 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################
    
def linea9():
    
    flujo = []
    nombres = []
    
    with open('Linea9.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#A52A2A'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 9')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 9 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()


#############################################################################################################

def lineaA():
    
    flujo = []
    nombres = []
    
    with open('LineaA.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#800080'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea A')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea A (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################

def lineaB():
    
    flujo = []
    nombres = []
    
    with open('LineaB.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = ['#008000','#808080','#008000','#808080','#008000','#808080','#008000','#808080','#008000','#808080',
             '#008000','#808080','#008000','#808080','#008000','#808080','#008000','#808080','#008000','#808080',
             '#008000']
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea B')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea B (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()

#############################################################################################################
  
def linea12():
    
    flujo = []
    nombres = []
    
    with open('Linea12.csv', 'r') as file:
        
        reader = csv.DictReader(file)
        
        for row in reader:
            f = float(row['Flujo'])
            n =  row['Nombre']
            flujo.append(f)
            nombres.append(n)
    
    color = '#FFD700'
    bars = plt.bar(nombres, flujo, color = color)
    
    plt.xlabel('Linea 12')
    plt.ylabel('Flujo total de personas (Millones)')
    plt.title('Flujo total de personas Linea 12 (2020)')
    
    for i, valor in enumerate(flujo):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=8, color='black')
        
    for bar, nombre in zip(bars, nombres):
        xval = bar.get_x() + bar.get_width() / 2
        yval = bar.get_height() / 2
        plt.text(xval, yval, f"{nombre}", ha='center', va='center', color='white', fontsize=8, rotation=90)
    
    plt.show()
