import requests
import json
import time

def menu():
    op = input('''\n################################################
#                     Menu                     #
################################################
#  Seja bem vindo(a) à sua lista de desejos    #
#  [1] Adicionar filme                         #
#  [2] Buscar filme na sua lista de desejos    #
#  [3] Listar filmes da sua lista de desejos   #
#  [4] Alterar status de um filme              #
#  [5] Exluir filme da sua lista de desejos    #
#  [0] Sair                                    #
################################################\n''').strip()
    if op == '1':
        add()
    elif op == '2':
        search()
    elif op == '3':
        show()
    elif op == '4':
        change()
    elif op == '5':
        delete()
    elif op == '0':
        print('Saindo...')
        time.sleep(2)
        exit
    else:
        print('Opção invalida!')
        menu()

def add():
    name = str(input('Digite o nome do filme: '.title()))
    response = requests.get('http://www.omdbapi.com/?apikey=f2c65418&t={}&y='.format(name)).json()

    try:

        dic = {
        'Titulo': response["Title"].lower(), 
        'Ano': response["Year"],
        'Tempo de filme': response["Runtime"],
        'Genero': response["Genre"],
        'Diretor': response["Director"],
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
        print('Escolha uma opção') 
        print('[1] Adicionar filme a lista de desejos')
        print('[2] Voltar ao menu')
        op = input('').strip()

        if op == '1':
            flag = True
            try:
                with open('movies.json') as files:
                    dados = json.load(files)

                for counter in dados:
                    if dic["Titulo"] == counter["Titulo"]:
                        flag = False

                if flag:
                    print('Deseja adicionar status ao filme?')
                    print('[1] Sim')
                    print('[2] Não')
                    opition = input('').strip()
                    if opition == '1':
                        print('Escolha um status para seu filme')
                        print('[1] Assistido')
                        print('[2] Assistir mais tarde')
                        print('[3] Continuar assistindo')
                        print('[4] Manter status pendente\n')
                        opition = input('').strip()
                        if opition == '1':
                            dic["Status"] = 'Assistido'
                            print('Filme marcado como assistindo')
                        elif opition == '2':
                            dic["Status"] = 'Assistir mais tarde'
                            print('Filme marcado como assistir mais tarde')
                        elif opition == '3':
                            dic["Status"] = 'Continuar assitindo'
                            print('Filme marcado como continuar assistindo')
                        elif opition == '4':
                            print('Status não alterado!')
                        else:
                            print('Opção invalida!\n')
                            time.sleep(1)
                            menu()
                    dados.append(dic)
                    with open ('movies.json', 'w') as files:
                        json.dump(dados, files, indent = 5)
                    print('Filme adicionado com sucesso!\n')
                    time.sleep(1)
                    menu()
                else:
                    print('O filme já foi cadastrado!\n')
                    time.sleep(1)
                    menu()

            except FileNotFoundError:
                if flag:
                    print('Deseja adicionar status ao filme?')
                    print('[1] Sim')
                    print('[2] Não')
                    opition = input('').strip()
                    if opition == '1':
                        print('Escolha um status para seu filme')
                        print('[1] Assistido')
                        print('[2] Assistir mais tarde')
                        print('[3] Continuar assistindo')
                        print('[4] Manter status pendente\n')
                        opition = input('').strip()
                        if opition == '1':
                            dic["Status"] = 'Assistido'
                            print('Filme marcado como assistindo')
                        elif opition == '2':
                            dic["Status"] = 'Assistir mais tarde'
                            print('Filme marcado como assistir mais tarde')
                        elif opition == '3':
                            dic["Status"] = 'Continuar assitindo'
                            print('Filme marcado como continuar assistindo')
                        elif opition == '4':
                            print('Status não alterado!')
                        else:
                            print('Opção invalida!\n')
                            time.sleep(1)
                            menu()
                    with open ('movies.json', 'w') as files:
                        json.dump(lista, files, indent = 5)
                    print('Filme adicionado com sucesso!\n')
                    time.sleep(1)
                    menu()
        elif op == '2':
            menu()
        else:
            print('Opção invalida!\n')
            time.sleep(1)
            menu()

    except KeyError:
        print('O filme não existe!\n')
        time.sleep(1)
        menu()

def search():
    name = input('Digite o nome do filme que deseja buscar: ').strip()
    flag = False

    try:
        with open('movies.json') as file:
            dados = json.load(file)

        for counter in dados:
            if counter["Titulo"] == name:
                lista = counter
                flag = True
            else:
                pass
        
        if flag == True:
            print('Titulo: ',lista["Titulo"])
            print('Ano:', lista['Ano'])
            print('Duração: ', lista['Tempo de filme'])
            print('Genero: ', lista['Genero'])
            print('Diretor: ',lista['Diretor'])
            print('Atores: ',lista['Atores'])
            print('Idioma: ', lista['Idioma'])
            print('Pais: ', lista['Pais'])
            print('Prêmios: ', lista['Premios'])
            print('Status:', lista["Status"])
            time.sleep(2)
            print('')
            menu()

        else:
            print('O filme não existe na sua lista de desejos!\n')
            time.sleep(2)
            menu()
    except FileNotFoundError:
        print('\nVocê ainda não possui uma lista de desejos')
        print('Volte ao menu para criar uma\n')
        time.sleep(2)
        menu()

def show():
    try:    
        with open('movies.json') as file:
            data = json.load(file)

        print('###########################################################')
        for counter in data:
            print('Titulo: ',counter["Titulo"])
            print('Ano:', counter['Ano'])
            print('Duração: ', counter['Tempo de filme'])
            print('Genero: ', counter['Genero'])
            print('Diretor: ',counter['Diretor'])
            print('Atores: ',counter['Atores'])
            print('Idioma: ', counter['Idioma'])
            print('Pais: ', counter['Pais'])
            print('Prêmios: ', counter['Premios'])
            print('Status', counter["Status"])
            print('###########################################################')
        time.sleep(2)
        menu()
    except FileNotFoundError:
        print('\nVocê ainda não possui uma lista de desejos')
        print('Volte ao menu para criar uma\n')
        time.sleep(2)
        menu()

def change():
    filme = input('Digite o nome do filme que deseja alterar: ')
    filme = filme.lower()
    flag = False

    try:
        with open('movies.json') as file:
            dados = json.load(file)

        for counter in dados:
            if filme == counter["Titulo"]:
                flag = True
                break

        if flag:
            print('Digite uma opção')
            print('[1] Assistido')
            print('[2] Assistir mais tarde')
            print('[3] Continuar assistindo\n')
            op = input('').strip()

            if op == '1':
                counter["Status"] = "Assistido"
                with open('movies.json', 'w') as file:
                    json.dump(dados, file, indent =  4)
                print('Status alterado para assistido\n')
                time.sleep(2)
                menu()
            elif op == '2':
                counter["Status"] = "Assistir mais tarde"
                with open('movies.json', 'w') as file:
                    json.dump(dados, file, indent = 4)
                print('Status alterado para assistir mais tarde\n')
                time.sleep(2)
                menu()
            elif op == '3':
                counter["Status"] = "Continuar assistindo"
                with open('movies.json', 'w') as file:
                    json.dump(dados, file, indent = 4)
                print('Status alterado para continuar assistindo\n')
                time.sleep(2)
                menu()
            else:
                print('Opção invalida\n')
                time.sleep(2)
                menu()
        else:
            print('O titulo digitado não existe em sua lista de desejos!\n')
            time.sleep(2)
            menu()
    except FileNotFoundError:
        print('\nVocê ainda não possui uma lista de desejos')
        print('Volte ao menu para criar uma\n')
        time.sleep(2)
        menu()        

def delete():
    filme = input('Digite o nome do filme à ser deletado: ').strip()
    filme = filme.lower()

    try:
        with open('movies.json') as file:
            dados = json.load(file)
            flag = False
            lista = []

            for counter in dados:
                if counter["Titulo"] == filme:
                    flag = True
                else:
                    pass

            if flag:
                for counter in dados:
                    if counter["Titulo"] != filme:
                        lista.append(counter)
                    else:
                        pass
                with open('movies.json', 'w') as file:
                    json.dump(lista, file, indent = 4)
                print('Filme excluido com sucesso\n')
                time.sleep(2)
                menu()
            else:
                print('O filme digitado não existe na sua lista de desejos\n')
                time.sleep(2)
                menu()
    except FileNotFoundError:
        print('\nVocê ainda não possui uma lista de desejos')
        print('Volte ao menu para criar uma\n')
        time.sleep(2)
        menu()

menu()         