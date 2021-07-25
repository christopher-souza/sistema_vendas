lista = []

def adicionar_nome(adicionar):
    lista.append(adicionar)

def remover_nome(remover):
     lista.remove(nome)


def idade_minima(idade):
    if int(idade) >= 16:
        return 'Pode votar'
    return 'Não pode votar'

def ultimo_nome():
    for i, n in enumerate(lista):
        print(n, i)

def sair():
    exit()

sair = True
while sair:
    print("1 para adicionar um nome na lista")
    print("2 para remover um nome da lista")
    print("3 para saber se tem idade para votar")
    print("4 para aparecer o último nome da lista")
    print('5 para sair')

    opcao = input("Escolher uma das opções")

    if int(opcao) == 1:
        nome = input("Qual nome deseja adicionar? \n")
        adicionar_nome(nome)

    elif int(opcao) == 2:
        remover = input("Qual nome deseja remover? \n")
        remover_nome(int(remover))

    elif int(opcao) == 3:
        idade = input("Sua idade \n")
        votar = idade_minima(int(idade))
        print(votar)

    elif int(opcao) == 4:
        ultimo_nome()

    elif int(opcao) == 5:
        sair()
