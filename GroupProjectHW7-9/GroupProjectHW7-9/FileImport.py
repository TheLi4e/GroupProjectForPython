import os
from Contacts import data


def ImportFromFile():
    global data
    if os.path.exists(r'phonebook.csv'):        
        with open(r'phonebook.csv', 'r') as f:
            imported_phonebook = f.read().strip()    
        for i in imported_phonebook.split('\n'):
            i = i.strip().split(',')
            data[i[0]] = i[1]
    else:
        data = {}
    return data
    
