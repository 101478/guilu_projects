import requests
import json
import time



def menu():
    op = input('''Seja bem vindo(a) à sua lista de desejos
    [1] Adicionar filme
    [2] Buscar filme
    [3] Alterar filme
    [4] Exluir filme
    [5] Sair\n''')
    if op == '1':
        adicionar()
    else:
        print('Saindo')
        exit
        

def adicionar():

    name = str(input('Digite o nome do filme: '.lower()))

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
        
    lista = [dic]
    op = input('Dejesa adicionar esse filme à lista de dejesos? ')

    if op == '1':

        flag = True
        try:

            with open('filmes.json') as files:
                dados = json.load(files)

            for c in dados:
                if dic["Titulo"] == c["Titulo"]:
                    flag = False

                else:
                    flag = True

            if flag:
                dados.append(dic)
                with open ('filmes.json', 'w') as files:
                    json.dump(dados, files, indent = 5)
                    print('Filme adicionado com sucesso!')
                    time.sleep(2)
                    menu()
            else:
                print('O filme já foi cadastrado! ')
                flag = False
                menu()

        except FileNotFoundError:
            with open ('filmes.json', 'w') as files:
                json.dump(dados, files, indent = 5)
                print('Filme adicionado com sucesso!')
                menu()


menu()         

