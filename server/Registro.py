from datetime import date, datetime
from pathlib import Path

def exibirHistorico(emissor,receptor):
    '''Classe que exibe o historico do emissor e do receptor'''
    contador = 0
    contadorLinhas = 0
    texto = ''
    try:
        arquivotexto = open(f'./{emissor}/{receptor}', 'r')
    except:
        texto = ''
        return texto
    else:
        arquivotexto.close()

    arquivotexto = open(f'./{emissor}/{receptor}', 'r')
    # FAZ A CONTAGEM DE LINHAS.
    for line in arquivotexto:
        contadorLinhas += 1
    arquivotexto.close()

    # COLOCA NA VARIAVEL O HISTORICO
    arquivotexto = open(f'./{emissor}/{receptor}', 'r')
    contadorLinhas = contadorLinhas - 10
    for line in arquivotexto:
        if (contador > contadorLinhas):
            texto = texto + line
        contador += 1
    return texto

def arquivoExiste(receptor,emissor):
    '''
    Verifica se um receptor já existe, se não o cria.
    :param receptor: receptor
    :param receptor: emissor
    :return:1 - Se o receptor já existe e 0 - se não existe
    '''
    try:
        a = open(f'./{emissor}/{receptor}', 'rt')
        a.close()
    except FileNotFoundError:
        return 0
    else:
        return 1

def usuarioRegistrado(emissor):
    '''
    Verifica se o usuario já foi registrado, isso é feito utilizando verificando se tem alguma pasta com o nome
    :param emissor: é o usuário que será verificado.
    :return:0 Se o usuario já tem pasta
    :return: -1 Se o usuário não possui pasta.
    '''
    import os
    lista = os.listdir(f'./')
    if emissor in lista:
        return 0
    else:
        return -1

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
            

def registro(emissor, receptor, mensagem):
    '''Faz o registro das conversas e os salva em disco.
    :param emissor: é o dono da conta do app
    :param receptor: é quem vai receber as mensagens
    :param mensagem: é a mensagem que o emissor irá trocar com o receptor
    :return:Até o momento, não retorna nada.'''

    # Cria a pasta do usuario, caso a pasta não exista
    Path(f'./{receptor}').mkdir(exist_ok=True)
    # Cria a pasta do usuario, caso a pasta não exista
    Path(f'./{emissor}').mkdir(exist_ok=True)

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
    dia = str(date.today())

    # Faz a busca da data no sistema, se a data não existe ele cria uma linha com a data Para o Emissor.
    if ((open(f'./{emissor}/{receptor}', 'r').read().find(dia)) == -1):
        a.writelines(f"{dia}\n")

    # Faz a busca da data no sistema, se a data não existe ele cria uma linha com a data Para o RECEPTOR
    if ((open(f'./{receptor}/{emissor}', 'r').read().find(dia)) == -1):
        b.writelines(f"{dia}\n")

    # Apresenta o historico desse usuário
    historico(receptor, emissor, dia)

    # Estrutura de teste, para simular uma conversa. O que as variaveis uteis: recepitor, emissor, mensagem, horario;
    a = open(f'./{emissor}/{receptor}', 'a')
    horario = datetime.now().strftime("%H:%M:%S")
    a.writelines(f"{horario} {emissor}: {mensagem}\n")
    a.close()

    # Faz as alterações no usuario receptor TAMBEM
    b = open(f'./{receptor}/{emissor}', 'a')
    b.writelines(f"{horario} {emissor}: {mensagem}\n")
    b.close()

def cadastro(emissor):
    import os
    Path(f'./{emissor}').mkdir(exist_ok=True)


