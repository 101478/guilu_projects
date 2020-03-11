import requests
import json
import time

def menu():
    op = input('''################################################
                      Menu
################################################
    Seja bem vindo(a) à sua lista de desejos
    [1] Adicionar filme
    [2] Buscar filme
    [3] Alterar filme
    [4] Exluir filme
    [5] Sair
################################################\n''')
    if op == '1':
        add()
    elif op == '2':
        search()
    elif op == '3':
        change()
    elif op == '4':
        delete()
    elif op == '5':
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
        print('Escolha uma opção') 
        print('[1] Adicionar filme a lista de tarefas')
        print('[2] Voltar ao menu')
        op = input('')

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
                    time.sleep(1)
                    menu()
                else:
                    print('O filme já foi cadastrado! ')
                    time.sleep(1)
                    menu()

            except FileNotFoundError:
                if flag:
                    with open ('filmes.json', 'w') as files:
                        json.dump(lista, files, indent = 5)
                    print('Filme adicionado com sucesso!')
                    time.sleep(1)
                    menu()
        elif op == '2':
            menu()
        else:
            print('Opção invalida!')
            time.sleep(1)
            menu()

    except KeyError:
        print('O filme não existe!')
        time.sleep(1)
        menu()

def search():
    name = input('Digite o nome do filme que deseja buscar: ')
    flag = False

    with open('filmes.json') as file:
        dados = json.load(file)

    for c in dados:
        if c["Titulo"] == name:
            lista = c
            flag = True
        else:
            pass
    
    if flag == True:
        print('Titulo: ',lista["Titulo"])
        print('Ano:', lista['Ano'])
        print('Duração: ', lista['Tempo de filme'])
        print('Genero: ', lista['Genero'])
        print('Diretor: ',lista['Director'])
        print('Atores: ',lista['Atores'])
        print('Idioma: ', lista['Idioma'])
        print('Pais: ', lista['Pais'])
        print('Prêmios: ', lista['Premios'])
        print('Status', lista["Status"])
        #print(json.dumps(lista, indent = 4))
        time.sleep(2)
        menu()

    else:
        print('O filme não existe na sua lista de desejos!')
        time.sleep(1)
        menu()

def change():
    filme = input('Digite o nome do filme que deseja alterar: ')
    flag = False

    with open('filmes.json') as file:
        dados = json.load(file)

    for c in dados:
        if filme == c["Titulo"]:
            flag = True
            break

    if flag:
        print('Digite uma opção')
        print('[1] Assistido')
        print('[2] Assistir mais tarde')
        print('[3] Continuar assistindo\n')
        op = input('')

        if op == '1':
            c["Status"] = "Assistido"
            with open('filmes.json', 'w') as file:
                json.dump(dados, file, indent =  4)
            print('Status alterado para assistido')
            time.sleep(1)
            menu()
        elif op == '2':
            c["Status"] = "Assistir mais tarde"
            with open('filmes.json', 'w') as file:
                json.dump(dados, file, indent = 4)
            print('Status alterado para assistir mais tarde')
            time.sleep(1)
            menu()
        elif op == '3':
            c["Status"] = "Continuar assistindo"
            with open('filmes.json', 'w') as file:
                json.dump(dados, file, indent = 4)
            print('Status alterado para continuar assistindo')
            time.sleep(1)
            menu()
        else:
            print('Opção invalida')
            time.sleep(1)
            menu()
    else:
        print('O titulo digitado não existe em sua lista de desejos!')
        time.sleep(1)
        menu()

def delete():
    filme = input('Digite o nome do filme à ser deletado: ')

    with open('filmes.json') as file:
        dados = json.load(file)
        flag = False
        lista = []

        for c in dados:
            if c["Titulo"] == filme:
                flag = True
            else:
                pass

        if flag:
            for c in dados:
                if c["Titulo"] != filme:
                    lista.append(c)
                else:
                    pass
            with open('filmes.json', 'w') as file:
                json.dump(lista, file, indent = 4)
            print('Filme excluido com sucesso')
            time.sleep(1)
            menu()
        else:
            print('O filme digitado não existe na sua lista de desejos\n')
            time.sleep(1)
            menu()

menu()         