# -*- coding: utf-8 -*-

class StationInfo:
    id = -1
    stationName = ""
    line = []
    transfer = ""
    cost = -1
    def __init__(self, to, name,line, transfer,c):
        self.id = to
        self.next = next
        self.cost = c
        self.stationName = name
        self.line = line
        self.transfer = transfer