
import requests
import json

response = requests.get('https://randomuser.me/api')
consulta = json.loads(response.text)


if (consulta['results'][0]['gender']) == "male":
    first=(consulta['results'][0]['name']['first'])
    last=(consulta['results'][0]['name']['last'])
    user=(consulta['results'][0]['login']['username'])
    password=(consulta['results'][0]['login']['password'])
    print("\nMan","\nNombre:",first ,"\nApellido:",last,"\nUser:",user,"\npassword:",password)
else:
    first=(consulta['results'][0]['name']['first'])
    last=(consulta['results'][0]['name']['last'])
    City=(consulta['results'][0]['location']['city'])
    street=(consulta['results'][0]['location']['street']['name'])
    numberstreet=(consulta['results'][0]['location']['street']['number'])
    print("\nWoman","\nNombre:",first, "\nApellido:",last,"\nCiudad",City,"\nCalle:",street,"\nNumeroCalle:",numberstreet,)

