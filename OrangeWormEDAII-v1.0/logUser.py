import time
import LoadingScreen

def logUser(loginSys):
    print(u"\u001b[38;5;202mINICIO DE SESION")
    print(u"\u001b[0m")
    username = input(u'\u001b[38;5;120mIngresa tu nombre de usuario:\u001b[0m ')
    userNode = loginSys.search(username)
    if userNode is not None:
        LoadingScreen.login(3)
        val = userNode.login()
        if val is True:
            return userNode
        else:
            return None
    else:
        LoadingScreen.login(2)
        print("La cuenta con el nombre de usuario "+username+" no existe!")
        time.sleep(1.5)
        return None