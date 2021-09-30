#Um jogo onde você precisa adivinhar qual número o computador está "pensando"
#Caso você encontre algum erro no código ou na execução, ficarei feliz em ser notificado :)

from random import randint
print('\033[1;33m-\033[m\033[1;34m-\033[m'*29)
print('                   \033[34mJOGO DA\033[m \033[33mADIVINHA\033[m\033[34mÇÃO\033[m')
print('\033[1;33m-\033[m\033[1;34m-\033[m'*29)
numero = int(input('Estou pensando em um número entre 0 e 10, adivinhe qual é: '))
computador = randint(0, 10)
while numero != computador:
    int(input(f'Eu pensei no número \033[31m{computador}\033[m 😎 tente de novo: '))
    computador = randint(0, 10)
else:
    print('\033[1;32mCaramba! Você acertou!!')