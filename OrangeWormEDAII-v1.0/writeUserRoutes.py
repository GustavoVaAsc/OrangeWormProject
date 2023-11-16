def writeUserRoutes(user):
    filename = user.name + "Routes.txt"
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.write("Name,First Station,Last Station,Transfer Time,Station Num\n")

        for route in user.routeList:
            file.write(
                f"{route.name},{route.firstStation},{route.lastStation},{route.transferTime},{route.stationNum}\n"
            )