import requests
import json
controlloop = ''
while controlloop != 1:
    print('===============================')
    print('====The Pokemon PythonDex======')
    inputpoke = input('please input Pokemon name: ').lower()
    if inputpoke == 'exit':
        break
    else:
        host = 'https://pokeapi.co/api/v2'

        pokename =f'/pokemon/{inputpoke}'



        pokeurl = host + pokename
        data = requests.get(pokeurl)
        try:
            data = data.json()
            # with open('poke.json','w') as dt:
            #     json.dump(data, dt)
            # with open ('poke.json','r') as js:
            #     dataImport = json.load(js)        
            # print(data)
            print((f'Pokemon Name: {inputpoke}').capitalize())
            pokestat = data['stats']
            print('Pokemon Stats: ')
            for i in pokestat:
                print(i['stat']['name'],(':'), i['base_stat'])
            poketype = data['types']
            print('Pokemon Type: ')
            for i in poketype:
                print(i['type']['name'])
            pokedata = data['abilities']
            print('Ability: ')
            for i in pokedata:
                print(i['ability']['name'])
        except:
            print('Pokemon not found, try again')