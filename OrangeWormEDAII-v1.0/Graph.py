from Station import Station
import heapq

class Graph:
    edges = []
    grade = []
    numNodes = 0
    numEdges = 0
    isDirected = False
    isTagged = False
    time = 0
    
    
    def __init__ (self, nodes, edges, isDirected, isTagged):
        self.numNodes = nodes
        self.numEdges = edges
        self.edges = []
        self.grade = []
        self.isTagged = isTagged
        self.isDirected = isDirected
        for i in range(0,nodes+1):
            self.grade.append(0)
            self.edges.append(None)

    def __str__ (self):
        item = None
        res = ""
        for i in range(1,self.numNodes+1):
            res += "\nNode #" + str(i) + " :\t"
            item = self.edges[i]
            j = 0
            while item != None:
                res += str(item.to) + ":" + str(item.cost) + "\t"
                item = item.next
        res += "\n"
        return res

    
    def addEdge(self, intU, intV, cost, isDirected, nameU, nameV, lineU, lineV, transfer):
        #print(intU,intV,cost, isDirected, nameU, nameV, lineU, lineV, transfer)
        newNode = Station(intV, self.edges[intU], cost,nameU,lineU, transfer)
        self.edges[intU] = newNode
        self.grade[intU] += 1

        if isDirected == False and intV != intU:
            self.addEdge(intV, intU, cost, True,nameV,nameU,lineV, lineU,transfer)

    
    def readEdges(self):
        for i in range(1,self.numEdges+1):
            u = int(input('U: '))
            v = int(input('V: '))
            if self.isTagged == True:
                cost = int(input('Weight: '))
            else:
                cost = 1
            self.addEdge(u, v, cost, False)
    
    def readEdgesList(self,listU,listV):
        for i in range(0,len(listU)):
            u = listU[i]
            v = listV[i]
            cost = 1
            self.addEdge(u, v, cost, False)
    
    
    def BFS(self, startNode, costs):
        self.edges[startNode].color = 1     
        self.edges[startNode].distance = 0   
        self.edges[startNode].prev = None    
        queue = []                           
        queue.append(startNode)              
        while len(queue) != 0:               
            u = queue.pop(0)                
            v = self.edges[u]                
            while v != None:
                #print(self.edges[u].stationName," ",self.edges[u].cost)            
                if self.edges[v.to] != None:                                   
                    if self.edges[v.to].color == 0:                            
                        self.edges[v.to].color = 1                              
                        self.edges[v.to].distance = self.edges[u].distance + 1  
                        self.edges[v.to].prev = u                               
                        queue.append(v.to)                                     
                v = v.next                                                     
            self.edges[u].color = 2                                             

    
    def printColor(self):
        print("BFS: ")
        res = ""
        for i in range(1,self.numNodes+1):
            if self.edges[i] != None:
                if self.edges[i].color == 0:
                    color = "White"
                elif self.edges[i].color == 1:
                    color = "Gray"
                else:
                    color = "Black"
                cont = 0
                tabs = ""
                while cont < self.edges[i].distance:
                    tabs +="\t"
                    cont += 1
                res += tabs + str(i) + ": " +  color + "-" + str(self.edges[i].distance) +" - "+ self.edges[i].stationName+"\t"
                res+="\n"
        print(res)
    
    def allNodesDFS(self):
        for i in range(1,self.numNodes+1):
            if self.edges[i] != None:
                if self.edges[i].color == 0:
                    self.DFS(i)


    def DFS(self, u):
        self.edges[u].color = 1 
        self.time += 1 
        self.edges[u].distance = self.time 
        
        v = self.edges[u]
        while v != None:
            if self.edges[v.to] != None: 
                if self.edges[v.to].color == 0:
                    self.edges[v.to].prev = self.edges[u] 
                    self.DFS(v.to)
            v = v.next 
        
        self.edges[u].color = 2 
        self.time += 1 
        self.edges[u].final = self.time
        

    
    def printColor2(self):
        print("DFS: ")
        res = ""
        for i in range(self.numNodes+1):
            if self.edges[i] != None:
                color = "blank" if self.edges[i].color == 0 else "gray" if self.edges[i].color == 1 else "black"
                res += str(i) + ": " + color + "-" + str(self.edges[i].distance) + "-" + str(self.edges[i].final) + "\t"
                res += "\n"
        
        print(res)
        
    def dijkstra(self, startNode):
        distances = [float('inf')] * (self.numNodes + 1)
        predecessors = [None] * (self.numNodes + 1)
        distances[startNode] = 0

        priorityQueue = [(0, startNode)]

        while priorityQueue:
            currentDistance, currentNode = heapq.heappop(priorityQueue)

            currentNeighbor = self.edges[currentNode]

            while currentNeighbor:
                neighborNode = currentNeighbor.to
                edgeWeight = currentNeighbor.cost

                if distances[currentNode] + edgeWeight < distances[neighborNode]:
                    distances[neighborNode] = distances[currentNode] + edgeWeight
                    predecessors[neighborNode] = currentNode
                    heapq.heappush(priorityQueue, (distances[neighborNode], neighborNode))

                currentNeighbor = currentNeighbor.next

        return distances[1:], predecessors
    
    def printRoute(self, startNode, endNode):
        distances, predecessors = self.dijkstra(startNode)
        

        print("Ruta para el trayecto {} - {}: TIEMPO DE TRASLADO {} min.".format(self.edges[startNode].stationName, self.edges[endNode].stationName, distances[endNode]))

        final_distance = distances[endNode]
        
        path = [endNode]
        while predecessors[endNode] is not None:
            endNode = predecessors[endNode]
            path.insert(0, endNode)

        station_names = [self.edges[node].stationName for node in path]
        print("Route: {}".format(" -> ".join(station_names)))
        
        return final_distance, len(path)
        

        
    def updateAllEdgesCosts(self, newCosts):
        #print(newCosts)
        for i in range(1, self.numNodes + 1):
            currentEdge = self.edges[i]
            while currentEdge is not None:
                #print(currentEdge.lines)
                currentEdge.cost += newCosts[currentEdge.lines-1]
                currentEdge = currentEdge.next

    def resetColors(self):
        for i in range(1, self.numNodes + 1):
            if self.edges[i] is not None:
                self.edges[i].color = 0
    
    
    # PENDING FOR CHECKING...
    
    
    def averageWeightDFS(self):
        total_weight = 0
        total_edges = 0

        for i in range(1, self.numNodes + 1):
            if self.edges[i] != None and self.edges[i].color == 0:
                weight, edges_count = self.DFSForAverageWeight(i)
                total_weight += weight
                total_edges += edges_count

        average_weight = total_weight / total_edges if total_edges > 0 else 0
        print(f"Average Weight of All Edges: {average_weight}")

    def DFSForAverageWeight(self, u):
        self.edges[u].color = 1
        self.time += 1
        self.edges[u].distance = self.time

        v = self.edges[u]
        weight = 0
        edges_count = 0

        while v != None:
            if self.edges[v.to] != None:
                if self.edges[v.to].color == 0:
                    edge_weight = v.cost
                    weight += edge_weight
                    edges_count += 1
                    self.edges[v.to].prev = self.edges[u]
                    w, c = self.DFSForAverageWeight(v.to)
                    weight += w
                    edges_count += c

            v = v.next

        self.edges[u].color = 2
        self.time += 1
        self.edges[u].final = self.time

        return weight, edges_count