import requests
import json
import datetime



def menu():
    op = input('''Seja bem vindo(a) à sua lista de desejos
    [1] Adicionar filme
    [2] Buscar filme
    [3] Alterar filme
    [4] Exluir filme''')
    if op == '1':
        escrever_json()
    else:
        print('Fim')

def escrever_json():

    name = str(input('Digite o nome do filme:'))

    response = requests.get('http://www.omdbapi.com/?apikey=f2c65418&t={}&y='.format(name)).json()

    dic = {
    'Titulo': response["Title"], 
    'Ano': response["Year"],
    'Duração': response["Runtime"],
    'Genero': response["Genre"],
    'Director': response["Director"],
    'Atores': response["Actors"],
    'Idioma': response["Language"],
    'Pais': response["Country"],
    'Prêmios': response["Awards"],
    'Status': 'Pendente'
     }

             

    print('Titulo: ',response['Title'])
    print('Ano:', response['Year'])
    print('Duração: ', response['Runtime'])
    print('Genero: ', response['Genre'])
    print('Diretor: ',response['Director'])
    print('Atores: ',response['Actors'])
    print('Idioma: ', response['Language'])
    print('Pais: ', response['Country'])
    print('Prêmios: ', response['Awards'])
    print('Status', dic["Status"])
        

    op = input('Dejesa adicionar esse filme à lista de dejesos?')
        
    if op == '1':
        with open ('filmes.json', 'a') as files:
            json.dump(dic, files, indent = 5)
        print('Filme adicionado com sucesso!')
        menu()
    else:
        print('Saindo')
        menu()

menu()          
