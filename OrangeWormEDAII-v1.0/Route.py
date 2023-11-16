class Route:
    name = ""
    firstStation = ""
    lastStation = ""
    transferTime = 0
    stationNum = 0
    
    def __init__(self,name,first,last,time,st):
        self.name = name
        self.firstStation = first
        self.lastStation = last
        self.transferTime = time
        self.stationNum = st