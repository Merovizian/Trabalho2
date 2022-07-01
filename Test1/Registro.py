from time import time
from datetime import date, datetime
from pathlib import Path

#Emissor é quem tem a conta no Materic
emissor = input("Quem é o usúario do Materic: ")

#O nome do receptor(receptor de texto) é o nome do seu contato
receptor = input("Para quem vai mandar as mensagens: ")

#Cria a pasta do usuario, caso a pasta não exista
Path(f'./{emissor}').mkdir(exist_ok=True)

dia = input("Que dia é hoje: ")

data_atual = str(date.today())
time_atual = time()
texto = list()
contador = 0
horario = datetime.now().strftime("%H:%M:%S")


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


#Verifica se existe arquivo na conta do Emissor, se tiver ele abre, se não tiver, ele cria.
if arquivoExiste(receptor,emissor) == 0:
    a = open(f'./{emissor}/{receptor}', 'wt+')
    print(f"Arquivo {receptor} criado com sucesso!")
else:
    a = open(f'./{emissor}/{receptor}', 'a')
    print(f"Arquivo {receptor} já existente")

#Verifica se existe arquivo na conta do Receptor, se tiver ele abre, se não tiver, ele cria.
if arquivoExiste(emissor,receptor) == 0:
    b = open(f'./{receptor}/{emissor}', 'wt+')
    print(f"Arquivo {emissor} criado com sucesso!")
else:
    b = open(f'./{receptor}/{emissor}', 'a')
    print(f"Arquivo {emissor} já existente")





#Faz a busca da data no sistema, se a data não existe ele cria uma linha com a data Para o Emissor.
if ((open(f'./{emissor}/{receptor}', 'r').read().find(dia)) == -1):
    a.writelines(f"{dia}\n")

# Faz a busca da data no sistema, se a data não existe ele cria uma linha com a data Para o RECEPTOR
if ((open(f'./{receptor}/{emissor}', 'r').read().find(dia)) == -1):
    b.writelines(f"{dia}\n")



#Apresenta o historico desse usuário
if (contador >= 0):
    historico(receptor, emissor, dia)
    contador = 2


#Estrutura de teste, para simular uma conversa. O que as variaveis uteis: recepitor, emissor, mensagem, horario;
while True:
    escolha = input(f"Quem esta escrevendo [1 - {emissor} 2 - {receptor} 3 - Sair do chat]: ")
    if (escolha == "1"):
        a = open(f'./{emissor}/{receptor}', 'a')
        mensagem = input(f"{emissor}: ")
        horario = datetime.now().strftime("%H:%M:%S")
        time_atual = time()
        a.writelines(f"{horario} {emissor}: {mensagem}\n")
        a.close()

        #Faz as alterações no usuario receptor TAMBEM
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
        print(f"Arquivo {receptor} gravado com sucesso!")
        break


'''
FALTA CRIAR O HISTORICO ANTITESE(salvar o historico na pasta de quem ta recebendo as mensagens.)

'''



