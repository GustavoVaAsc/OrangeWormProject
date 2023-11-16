from User import User

def readAccounts(loginSys,file_path="accounts.txt"):

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name, password, isAdmin = data[0], data[1], bool(int(data[2]))
            new_user = User(name, password, isAdmin)
            loginSys.insert(new_user)
    return