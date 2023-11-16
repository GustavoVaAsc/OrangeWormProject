import csv

def sobreescribirUsuarios(filename, btreeAccounts):
    
    data_list = []
    btreeAccounts.traverseSave(data_list)
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for data in data_list:
            if data.isAdmin == False:
                tmp = 0
            else:
                tmp = 1
            writer.writerow([data.name, data.password, tmp])
