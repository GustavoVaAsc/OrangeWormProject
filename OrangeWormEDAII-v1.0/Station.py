class Station:
    to = 0
    cost = 0
    next = None
    prev = None
    color = 0
    distance = -1
    final = -1
    stationName = ""
    lines = 0
    transfer = ""
    def __init__(self, to, next, c,name,line, transfer):
        self.to = to
        self.next = next
        self.cost = c
        self.stationName = name
        self.lines = line
        self.transfer = transfer
