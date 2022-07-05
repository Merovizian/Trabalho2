'''Classe que exibe o historico do emissor e do receptor'''
contador = 0
emissor = "Eric"
receptor = "Mateus"
contadorLinhas = 0
texto = list()

arquivotexto = open(f'./{emissor}/{receptor}', 'r')

for line in arquivotexto:
    contadorLinhas += 1
arquivotexto.close()

arquivotexto = open(f'./{emissor}/{receptor}', 'r')
contadorLinhas = contadorLinhas - 8
for line in arquivotexto:
    if (contador > contadorLinhas):
        texto.append(line)
    contador += 1
return texto


print(texto)




'''
try:
    arquivotexto = open(f'./{emissor}/{receptor}', 'r')
except:
    texto = ""
    return texto
texto = arquivotexto.read()
if texto == None:
    texto = ''

for line in texto:
    contador += 1
    if (contador >= localizacao and localizacao != -1):
        print(line)

    return texto'''