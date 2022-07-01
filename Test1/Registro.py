from time import time
from datetime import date, datetime
from pathlib import Path


emissor = input("Quem é o usúario do Materic: ")
receptor = input("Para quem vai mandar as mensagens: ")

#Cria a pasta do usuario, caso a pasta não exista
Path(f'./{emissor}').mkdir(exist_ok=True)

dia = input("Que dia é hoje: ")

data_atual = str(date.today())
time_atual = time()
texto = list()

horario = datetime.now().strftime("%H:%M:%S")


def arquivoExiste(nome):
    '''
    Verifica se um arquivo já existe, se não o cria.
    :param nome: arquivo
    :return:1 - Se o arquivo já existe e 0 - se não existe
    '''
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return 0
    else:
        return 1

#O nome do arquivo(arquivo de texto) é o nome do seu contato
arquivo = receptor
if arquivoExiste(arquivo) == 0:
    a = open(arquivo, 'wt+')
    print(f"Arquivo {arquivo} criado com sucesso!")
else:
    a = open(arquivo, 'a')
    print(f"Arquivo {arquivo} já existente")

#Faz a busca da data no sistema, se a data não existe ele cria uma linha com a data.
if ((open(f'{arquivo}', 'r').read().find(dia)) != 0):
    a.writelines(f"{dia}\n")

#Estrutura de teste, para simular uma conversa. O que as variaveis uteis: recepitor, emissor, mensagem, horario;
while True:
    escolha = input("Quem esta escrevendo [1 - Eric 2 - Mateus 3 - Sair do chat]: ")
    if (escolha == "1"):
        mensagem = input("Eric: ")
        horario = datetime.now().strftime("%H:%M:%S")
        time_atual = time()
        a.writelines(f"{horario} {emissor}: {mensagem}\n")
    if (escolha == "2"):
        mensagem = input("Mateus: ")
        horario = datetime.now().strftime("%H:%M:%S")
        time_atual = time()
        a.writelines(f"{horario} {receptor}: {mensagem}\n")
    if (escolha == "3"):
        a.close()
        print(f"Arquivo {arquivo} gravado com sucesso!")
        break



