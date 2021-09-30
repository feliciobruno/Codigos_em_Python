#um programa simples de contagem regressiva em Python...
#Caso haja algum erro na codificação ou na execução, ficarei feliz em saber :)

from time import sleep
print('\033[34m===\033[m' *20)
print('\033[1;33m             CONTAGEM REGRESSIVA DO DESAFIO\033[m')
print('\033[34m===\033[m' *20)
numero = int(input('Digite em quantos segundos será a contagem (apenas números): '))
for contagem in range(numero, 0, -1):
    print(contagem, end='')
    if contagem % 2 == 0:
        print('\033[31m')
    else:
        print('\033[33m')
    segundos = sleep(1)
print('\033[31mFim! Seu tempo acabou!\033[m')