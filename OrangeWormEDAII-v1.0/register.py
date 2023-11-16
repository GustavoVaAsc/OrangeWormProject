from User import User
import LoadingScreen
import time
import Sobreescribir

def register(loginSys):
    flag = False
    while flag is False:
        print(u"\u001b[38;5;202mREGISTRO DE USUARIO")
        print(u"\u001b[0m")
        username = input("Ingresa un nombre de usuario: ")
        wrong = False
        while wrong is False:
            password = input("Ingresa tu contraseña: ")
            cpass = input("Confirma tu contraseña: ")
            if password == cpass:
                newUser = User(username,password,0)
                loginSys.insert(newUser)
                Sobreescribir.sobreescribirUsuarios('accounts.txt',loginSys)
                LoadingScreen.login(4)
                time.sleep(1.5)
                flag = True
                wrong = True
            else:
                LoadingScreen.login(5)
        