import requests
import json
import time

def menu():
    op = int(input('''################################################
                      Menu
################################################
    Seja bem vindo(a) à sua lista de desejos
    [1] Adicionar filme
    [2] Buscar filme
    [3] Alterar filme
    [4] Exluir filme
    [5] Sair
################################################\n'''))
    if op == 1:
        adicionar()
    elif op == 2:
        buscar()
    elif op == 3:
        alterar()
    else:
        print('Saindo')
        exit

def adicionar():
    name = str(input('Digite o nome do filme: '.title()))
    response = requests.get('http://www.omdbapi.com/?apikey=f2c65418&t={}&y='.format(name)).json()
    flag = True

    if response == 'False':
        flag = False

    if flag:
        dic = {
        'Titulo': response["Title"], 
        'Ano': response["Year"],
        'Tempo de filme': response["Runtime"],
        'Genero': response["Genre"],
        'Director': response["Director"],
        'Atores': response["Actors"],
        'Idioma': response["Language"],
        'Pais': response["Country"],
        'Premios': response["Awards"],
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
        op = input('''Escolha uma opção 
        [1] Adicionar filme a lista de tarefas
        [2] Voltar ao menu ''')

        if op == '1':

            flag = True
            try:
                with open('filmes.json') as files:
                    dados = json.load(files)

                for c in dados:
                    if dic["Titulo"] == c["Titulo"]:
                        flag = False

                if flag:
                    dados.append(dic)
                    with open ('filmes.json', 'w') as files:
                        json.dump(dados, files, indent = 5)
                    print('Filme adicionado com sucesso!')
                    time.sleep(2)
                    menu()
                else:
                    print('O filme já foi cadastrado! ')
                    menu()

            except FileNotFoundError:
                if flag:
                    with open ('filmes.json', 'w') as files:
                        json.dump(lista, files, indent = 5)
                    print('Filme adicionado com sucesso!')
                    menu()
        else:
            menu()
    else:
        print('O filme não existe!')

def buscar():
    name = input('Digite o nome do filme que deseja buscar: ')
    name = name.title()
    flag = False

    with open('filmes.json') as file:
        dados = json.load(file)

    for c in dados:
        if c["Titulo"] == name:
            lista = [c]
            flag = True
    
    if flag == True:
        print(json.dumps(lista, indent = 4))
        time.sleep(2)
        print('')
        print('')
        menu()

    elif flag == False:
        print('O filme não existe na sua lista de desejos!')
        time.sleep(2)
        print('')
        print('')
        menu()

def alterar():
    filme = input('Digite o nome do filme que deseja alterar: ')
    filme = filme.title()
    flag = False

    with open('filmes.json') as file:
        dados = json.load(file)

    for c in dados:
        if filme == c["Titulo"]:
            c["Titulo"] = filme
            flag = True

    if flag:
        op = int(input('''Digite uma opção
        [1] Assistido
        [2] Assistir mais tarde
        [3] Continuar assistindo\n'''))

        if op == 1:
            c["Status"] = "Assistido"
            with open('filmes.json') as file:
                json.dump(dados, file, indent =  4)
            print('Status alterado!')
        elif op == 2:
            print('Teste2')
        elif op == 3:
            print('Teste3')

        menu()
    else:
        print('O titulo digitado não existe em sua lista de desejos!')
        time.sleep(2)
        menu()

def deletar():
    filme = input('Digite o nome do filme à ser deletado: ')
    filme = filme.title()
    flag = False

    with open('filmes.json') as file:
        dados = json.load(file)

        for c in dados:
            if c["Titulo"] == filme:
                flag = True


menu()         

