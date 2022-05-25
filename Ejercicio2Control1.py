from mailbox import NoSuchMailboxError
import requests
import json


def georeference(n):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    consulta = json.loads(response.text)
    list=[]
    n=(input("ingrese un numero:"))
    nombre=(consulta[int(n)]['name'])
    latitud=(consulta[int(n)]['address']['geo']['lat'])
    longitud=(consulta[int(n)]['address']['geo']['lng'])
    list.append([nombre])
    list.append([latitud])
    list.append([longitud])
    return list
    
n=0
print(georeference(n))
