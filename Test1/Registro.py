from time import time
from datetime import date, datetime
from pathlib import Path
import os

def exibirHistorico(emissor, receptor):
    '''Classe que exibe o historico do emissor e do receptor'''
    arquivotexto = open(f'./{emissor}/{receptor}', 'r')
    texto = arquivotexto.read().split("\n")
    for line in texto:
        print(line)

def arquivoExiste(receptor,emissor):
    '''
    Verifica se um receptor já existe, se não o cria.
    :param nome: receptor
    :return:1 - Se o receptor já existe e 0 - se não existe
    '''
    try:
        a = open(f'./{emissor}/{receptor}', 'rt')
        a.close()
    except FileNotFoundError:
        return 0
    else:
        return 1

def historico(receptor,emissor,data):
    '''Verifica se há um historico no sistema do receptor, se houve, as mensagens do dia de hoje.
    se não houve retorna que não há historico.
    :param emissor: é o dono da conta do app
    :param receptor: é quem vai receber as mensagens
    :param data: O dia de hoje, a partir daí o histórico será apresentado.
    :return:Até o momento, não retorna nada.'''
    arquivotexto = open(f'./{emissor}/{receptor}', 'r')
    texto = arquivotexto.read().split("\n")
    contador = 0
    with open(f'./{emissor}/{receptor}', 'r') as f:
        for localizacao, l in enumerate(f, 1): # percorrer linhas e enumera-las a partir de 1
            if data in l: # ver se palavra esta na linha
                localizacao
                break
        else: localizacao = -1
    f.close()
    for line in texto:
        contador += 1
        if (contador >= localizacao and localizacao != -1 ):
            print(line)

def registro(emissor, receptor, mensagem=''):
    '''Faz o registro das conversas e os salva em disco.
    :param emissor: é o dono da conta do app
    :param receptor: é quem vai receber as mensagens
    :param mensagem: é a mensagem que o emissor irá trocar com o receptor
    :return:Até o momento, não retorna nada.'''

    # Cria a pasta do usuario, caso a pasta não exista
    Path(f'./{emissor}').mkdir(exist_ok=True)
    # Cria a pasta do usuario, caso a pasta não exista
    Path(f'./{receptor}').mkdir(exist_ok=True)



    # Verifica se existe arquivo na conta do Emissor, se tiver ele abre, se não tiver, ele cria.
    if arquivoExiste(receptor, emissor) == 0:
        a = open(f'./{emissor}/{receptor}', 'wt+')
    else:
        a = open(f'./{emissor}/{receptor}', 'a')

    # Verifica se existe arquivo na conta do Receptor, se tiver ele abre, se não tiver, ele cria.
    if arquivoExiste(emissor, receptor) == 0:
        b = open(f'./{receptor}/{emissor}', 'wt+')
    else:
        b = open(f'./{receptor}/{emissor}', 'a')


    #CRIA UMA VARIAVEL DE DATA TEMPORARIO PARA PODER TESTAR O SISTEMA
    dia = input("qual a data de hoje: ")

    # Faz a busca da data no sistema, se a data não existe ele cria uma linha com a data Para o Emissor.
    if ((open(f'./{emissor}/{receptor}', 'r').read().find(dia)) == -1):
        a.writelines(f"{dia}\n")

    # Faz a busca da data no sistema, se a data não existe ele cria uma linha com a data Para o RECEPTOR
    if ((open(f'./{receptor}/{emissor}', 'r').read().find(dia)) == -1):
        b.writelines(f"{dia}\n")

    # Apresenta o historico desse usuário
    historico(receptor, emissor, dia)

    # Estrutura de teste, para simular uma conversa. O que as variaveis uteis: recepitor, emissor, mensagem, horario;
    while True:
        escolha = input(f"Quem esta escrevendo [1 - {emissor} 2 - {receptor} 3 - Sair do chat]: ")
        if (escolha == "1"):
            a = open(f'./{emissor}/{receptor}', 'a')
            mensagem = input(f"{emissor}: ")
            horario = datetime.now().strftime("%H:%M:%S")
            time_atual = time()
            a.writelines(f"{horario} {emissor}: {mensagem}\n")
            a.close()

            # Faz as alterações no usuario receptor TAMBEM
            b = open(f'./{receptor}/{emissor}', 'a')
            b.writelines(f"{horario} {emissor}: {mensagem}\n")
            b.close()

        if (escolha == "2"):
            a = open(f'./{emissor}/{receptor}', 'a')

            mensagem = input(f"{receptor}: ")
            horario = datetime.now().strftime("%H:%M:%S")
            time_atual = time()
            a.writelines(f"{horario} {receptor}: {mensagem}\n")
            a.close()

            b = open(f'./{receptor}/{emissor}', 'a')
            b.writelines(f"{horario} {receptor}: {mensagem}\n")
            b.close()

        if (escolha == "3"):
            a.close()
            break

def menu():
    '''Cria um menu de interação'''
    print(f"\033[;1m{'MATERIC - TROCA DE MENSAGENS':*^70}\033[m")
    print("DIGITE A OPÇÃO DESEJADA")
    print("1 - login")
    print("2 - cadastro de nova conta")

def login():
    '''Cria um menu de interação'''
    os.system('cls')
    print(f"\033[;1m{'MATERIC - LOGIN'}\033[m")
    emissor = input("Informe o nome do usuario: ")
    usuario(emissor)

def usuario(emissor):
    ''' MENU DO USUARIO'''
    while True:
        os.system('cls')
        print(f"\033[;1m{'MATERIC - TROCA DE MENSAGENS':*^70}\033[m")
        print(f"BEM VINDO {emissor}")
        print("DIGITE A OPÇÃO DESEJADA")
        print("1 - Trocar mensagens: ")
        print("2 - Exibir histórico: ")
        print("0 - Sair da conta")
        escolha = input("Digite a opção desejada: ")
        if escolha == "0":
            break
        if escolha == "1":
            receptor = input("Com quem deseja conversar: ")
            registro(emissor, receptor)
        if escolha == "2":
            receptor = input("Historico de qual contato: ")
            exibirHistorico(emissor, receptor)
            input("Aperte Enter para Sair...")

def cadastro():
    '''Cria um menu de interação'''
    print(f"\033[;1m{'MATERIC - CADASTRAR NOVA CONTA'}\033[m")

while True:
    menu()
    choise = input("Digite a opção desejada: ")
    if (choise== "1"):
        login()
    elif (choise == "2"):
        cadastro()
    else:
        choise = input("Opção inválida, por valor escolha a opção correta: ")

