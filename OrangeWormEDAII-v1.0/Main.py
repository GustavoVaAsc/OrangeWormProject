import LoadingScreen
import MainMenu
import time
from BTree import BTree
from loginMenu import loginMenu
import cs
import initSubway
import time

def main():

    loginSys = BTree(100)
    flag = True
    logged = None
    subway,subwayDict,lineTimes = initSubway.initSubway()
    
    LoadingScreen.start()
    time.sleep(0.7)
    
    while flag is True:
        cs.clear()
        logged = loginMenu(loginSys)
        
        if logged is not None:
            cs.clear()
            LoadingScreen.curiosidades()
            MainMenu.menu(logged, loginSys, subway, subwayDict, lineTimes)
        else:
            flag = False 
            

main()




