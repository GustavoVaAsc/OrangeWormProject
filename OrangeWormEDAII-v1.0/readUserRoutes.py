from Route import Route

def readUserRoutes(user):
    routes = []
    filename = user.name + "Routes.txt"
    
    with open(filename, 'r', encoding = 'utf-8') as file:
        # Skip header
        next(file)

        # Read data
        for line in file:
            values = line.strip().split(',')
            name, first, last, transfer_time, station_num = values
            route = Route(name, first, last, int(transfer_time), int(station_num))
            routes.append(route)
    
    return routes